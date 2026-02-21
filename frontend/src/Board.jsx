import React from 'react'

const PIECE_MAP = {
  'P': '♙',
  'N': '♘',
  'B': '♗',
  'R': '♖',
  'Q': '♕',
  'K': '♔',
  'p': '♟',
  'n': '♞',
  'b': '♝',
  'r': '♜',
  'q': '♛',
  'k': '♚'
}

function parseFen(fen) {
  // Very lightweight parser for the starting portion of FEN (piece placement)
  const parts = fen.split(' ')
  const boardPart = parts[0]
  const rows = boardPart.split('/')
  const board = []
  for (let r = 0; r < 8; r++) {
    const row = rows[r]
    let cols = []
    for (let i = 0; i < row.length; i++) {
      const ch = row[i]
      if (isNaN(parseInt(ch, 10))) {
        cols.push(ch)
      } else {
        const empty = parseInt(ch, 10)
        for (let k = 0; k < empty; k++) cols.push(null)
      }
    }
    board.push(cols)
  }
  return board
}

export default function Board({ fen }) {
  const board = parseFen(fen)
  return (
    <div style={{ display: 'inline-block', border: '2px solid #333' }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(8, 40px)', border: '1px solid #000' }}>
        {board.flat().map((sq, idx) => {
          const isLight = ((idx + Math.floor(idx / 8)) % 2) === 0
          const bg = isLight ? '#f0d9b5' : '#b58863'
          const piece = sq
          return (
            <div key={idx} style={{ width: 40, height: 40, background: bg, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ fontSize: 20 }}>{piece ? PIECE_MAP[piece] : ''}</span>
            </div>
          )
        })}
      </div>
    </div>
  )
}
