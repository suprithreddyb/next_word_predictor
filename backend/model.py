import torch
import torch.nn as nn
import pickle


# device
device = "cpu"

# max length of tokens
max_len = 44

# Load vocab
with open("backend/vocab.pkl", "rb") as f:
  data = pickle.load(f)

vocab = data["vocab"]
reverse_vocab = data["reverse_vocab"]

# Model definition
class LSTM(nn.Module):
    def __init__(self, vocab_size):
      super().__init__()
      self.embedding = nn.Embedding(vocab_size, 100)
      self.lstm = nn.LSTM(100, 150, batch_first=True)
      self.linear = nn.Linear(150, vocab_size)

    def forward(self, x):
      x = self.embedding(x)
      _, (final_hidden, _) = self.lstm(x)
      output = self.linear(final_hidden.squeeze(0))
      return output

# Load model
model = LSTM(len(vocab))
model.load_state_dict(torch.load("backend/model.pth", map_location=device))
model.to(device)
model.eval()

# Tokenize
def tokenize( sentence ):
  sentence = sentence.lower()
  out = []
  for word in sentence.split():
    out.append( vocab.get( word, vocab[ "<UNK>" ] ) )
  return out

# Predict next word
def predict(text):
  if len( text.strip() ) == 0:
    return ""
  tokens = tokenize(text )
  tokens = tokens[-max_len:]
  pad_len = max_len - len(tokens)
  tokens = [vocab["<PAD>"]] * pad_len + tokens
  x = torch.tensor(tokens, dtype=torch.long).unsqueeze(0).to(device)
  with torch.no_grad():
    output = model(x)
    next_idx = torch.argmax(output, dim=1).item()
  return reverse_vocab[next_idx]