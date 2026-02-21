import React, { useState, useEffect } from 'react'
import Board from './Board.jsx'

function App() {
  const [fen, setFen] = useState('startpos');
  useEffect(() => {
    // Placeholder: in a real app, fetch initial game state from backend
    // For MVP, use standard initial FEN
    setFen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Dinosaur Chess – MVP</h1>
      <Board fen={fen} onHint={() => {}} />
      <p style={{ marginTop: 16 }}>
        This frontend is a minimal scaffold illustrating the dinosaur-themed board.
      </p>
    </div>
  )
}

export default App
