# Next Word Predictor Web App

A minimal web application that predicts the next word as you type using an LSTM model. Users can see the predicted word and insert it with **Tab** or by clicking it.

## Features

- Next-word prediction using a trained LSTM model
- Continuous predictions: accepts a suggestion and immediately predicts the next word
- Tab or click to insert predicted words
- Simple React frontend and FastAPI backend
- Minimalistic, easy-to-run setup


## Folder Structure

nextword_web_app/
├── backend/
│ ├── app.py 
│ ├── model.py
│ ├── model.pth
│ └── vocab.pkl
├── frontend/
│ ├── src/
│ │ ├── App.js
│ │ ├── App.css
│ │ └── index.js
│ ├── package.json
└── README.md


## Backend Setup

1. Navigate to the backend folder:

```bash
cd backend

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Install required packages:
pip install torch fastapi uvicorn

Run the backend server:
uvicorn app:app --reload
The backend will run on: http://127.0.0.1:8000

Test endpoint:
http://127.0.0.1:8000/predict?text=hello
It should return JSON:
{"next_word": "<next word>"}

Frontend Setup

Navigate to the frontend folder:
cd frontend

Install dependencies:

npm install
npm install axios
Run the frontend:
npm start

Opens on http://localhost:3000

Type in the input box and see the predicted next word

Press Tab or click the suggestion to insert it

Usage
Start backend first (uvicorn backend.app:app --reload)

Start frontend (npm start)

Open browser at http://localhost:3000

Type text → predicted word appears → accept with Tab or click

Repeat to continue predicting next words
