[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Unified Dinosaur Chess App — MVP

A single-player dinosaur-themed chess MVP with AI opponent. Frontend in React, backend in Python (Flask).

## Architecture at a glance
- Frontend: React SPA with a reusable component structure and context-based game state. REST-first for MVP with a ready path for WebSocket integration in the future.
- Backend: RESTful API (Flask) backed by a lightweight (SQLite/SQLAlchemy) data model. Server-side move validation and an AI opponent using a depth-limited minimax evaluator backed by the python-chess library.
- Game logic: Standard chess rules with dinosaur-themed visuals. All moves are validated on the server. AI supports Easy/Medium/Hard depths.
- Data model: Users, Games, and Moves. Game state stored as JSON-friendly FEN representation for flexibility and evolution.

## Setup

### Prerequisites
- Python 3.9+
- Node.js 18+ (for frontend)
- Optional: PostgreSQL in production (MPO-friendly; MVP uses SQLite for simplicity)

### Backend setup
1. Create a virtual environment and install dependencies
   - python -m venv venv
   - source venv/bin/activate  # Linux/macOS
   - venv\Scripts\activate     # Windows
   - pip install -r requirements.txt
2. Run the Flask app (development)
   - export FLASK_APP=backend.app
   - flask run --reload
3. Endpoints (MVP)
   - POST /games
   - GET /games/{game_id}
   - POST /games/{game_id}/moves
   - GET /games/{game_id}/over
   - GET /games/{game_id}/history

### Frontend setup
1. cd frontend
2. npm install
3. npm run dev

### Testing
- Backend tests use pytest. Install test dependencies and run:
  - pytest

### Architecture notes
- The MVP focuses on a single-player game against AI with dinosaur-themed visuals.
- Online multiplayer and advanced features are planned but out of scope for MVP.
- Security: JWT-based authentication tokens are prepared for REST with token forwarding on requests.

## Open Source & Contributions
This project is open source under the MIT license. Contributions are welcome. See LICENSE for details.

## References
- python-chess (https://pypi.org/project/python-chess/)
- Flask (https://flask.palletsprojects.com)
- React (https://reactjs.org)
