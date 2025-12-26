from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.model import predict  # make sure your model.py is in backend/
import uvicorn

app = FastAPI()

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def get_prediction(text: str = Query(..., min_length=1)):
    """
    Returns the next word prediction as JSON
    """
    next_word = predict(text)
    return {"next_word": next_word}


# Optional: run directly with `python app.py`
if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
