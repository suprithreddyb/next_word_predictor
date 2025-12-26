import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [suggestion, setSuggestion] = useState("");

  const fetchSuggestion = async (currentText) => {
    if (!currentText.trim()) {
      setSuggestion("");
      return;
    }
    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/predict?text=${encodeURIComponent(currentText)}`
      );
      setSuggestion(res.data.next_word);
    } catch (err) {
      console.error(err);
      setSuggestion("");
    }
  };

  const handleChange = (e) => {
    const value = e.target.value;
    setText(value);
    fetchSuggestion(value);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Tab" && suggestion) {
      e.preventDefault();
      const newText = text + " " + suggestion;
      setText(newText);
      // Immediately fetch next prediction
      fetchSuggestion(newText);
    }
  };

  const handleSuggestionClick = () => {
    const newText = text + " " + suggestion + " ";
    setText(newText);
    fetchSuggestion(newText); // fetch next prediction after click
  };

  return (
    <div className="container">
      <h1>Next Word Predictor</h1>
      <input
        type="text"
        value={text}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
        className="text-input"
        placeholder="Type here..."
        autoComplete="off"
      />
      {suggestion && text && (
        <div className="suggestion">
          Next word:{" "}
          <span className="ghost-word" onClick={handleSuggestionClick}>
            {suggestion}
          </span>
        </div>
      )}
    </div>
  );
}

export default App;
