# Next Word Predictor Web App

A minimal full-stack web application that predicts the **next word** in a sentence using a **PyTorch LSTM language model**.  
Users can type text into a textbox, see a **ghost (grey) next-word suggestion**, and press **Tab** to accept it — similar to modern autocomplete systems.

---

## Features

- LSTM-based next word prediction (PyTorch)
- Real-time predictions as you type
- Ghost text suggestion UI
- Tab key to accept predictions
- Python backend (Flask)
- React frontend
- Clean separation of frontend and backend

---

## Tech Stack

### Backend
- Python
- PyTorch
- Flask
- Flask-CORS

### Frontend
- React
- Axios
- CSS

---

## How It Works

1. User types text in the frontend
2. Frontend sends the current sentence to the backend
3. Backend:
   - Tokenizes input
   - Pads/truncates to fixed length
   - Runs inference using the trained LSTM
   - Returns the predicted next word
4. Frontend displays the prediction as ghost text
5. Pressing **Tab** accepts the prediction and triggers the next one

---

## Running the Project Locally

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd nextword_web_app
```
### 2. Start the backend
```bash
cd backend
python app.py
```
backend runs at: http://127.0.0.1:5000

### 3. Start the frontend (new terminal)
```bash
cd frontend
npm install
npm start
```
Frontend runs at: http://localhost:3000


## Model Details

Architecture: Embedding → LSTM → Linear

Loss: Cross Entropy Loss

Task: Next word prediction

Input: Tokenized sentence (fixed max length)

Output: Probability distribution over vocabulary


## Model Training

The language model was trained using a **Long Short-Term Memory (LSTM)** network implemented in **PyTorch**. 

### Training Dataset

The dataset is a human conversational dataset obtained from kaggle.
Dataset: https://www.kaggle.com/datasets/projjal1/human-conversation-training-data

### Training Workflow
- Text data was preprocessed by:
  - Lowercasing
  - Tokenizing into words
  - Building a vocabulary with `<PAD>` and `<UNK>` tokens
- Input sequences were padded or truncated to a fixed maximum length.
- The model was trained to predict the **next word** given a sequence of previous words.

### Training Setup
- Loss Function: **Cross Entropy Loss**
- Optimizer: **Adam**
- Batch size: 32
- epochs: 50
- Final training loss converged to  **0.550**, indicating effective learning of language patterns

### Training Environment
- Model training was performed in **Google Colab**
- GPU acceleration was used to speed up training
- Trained weights and vocabulary were exported and reused in the deployed web application

The trained model is loaded in inference mode for the web application to provide real-time next word predictions.

### Training Notebook

The complete model training workflow is available in training/training.ipynb.

## Future Improvements

top-k sampling

Larger dataset

Deployment (Vercel + Render)

Mobile-friendly UI

## Author
Built by Suprith For learning, experimentation, and showcasing ML + full-stack skills.