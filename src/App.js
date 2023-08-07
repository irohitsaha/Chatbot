import React, { useState } from 'react';
import './App.css';

function App() {
  const [userInput, setUserInput] = useState('');
  const [chatLog, setChatLog] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userInput) return;

    try {
      const response = await fetch('http://localhost:5000/chatbot', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  body: JSON.stringify({ prompt: userInput }),
});


      const data = await response.json();
      setChatLog((prevChatLog) => [
        ...prevChatLog,
        { user: userInput, bot: data.response },
      ]);

      setUserInput('');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1 >Chatbot App</h1>
      <div className="chat-container">
        {chatLog.map((entry, index) => (
          <div key={index}>
            <p><strong>You:</strong> {entry.user}</p>
            <p><strong>Chatbot:</strong> {entry.bot}</p>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Type your query..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
