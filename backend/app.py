from flask import Flask, request, jsonify
from backend.engine import create_initial_state, apply_move
from backend.ai import ai_move_for_fen

app = Flask(__name__)

# Simple in-memory store for MVP (not persistent across restarts)
GAMES = {}
GAME_COUNTER = 1

@app.route('/games', methods=['POST'])
def new_game():
    global GAME_COUNTER
    # In a full implementation, parse user auth and preferences
    initial = create_initial_state()
    game_id = GAME_COUNTER
    GAME_COUNTER += 1
    # White (player) vs AI (Black)
    GAMES[game_id] = {
        'fen': initial['fen'],
        'turn': initial['turn'],
        'moves': []
    }
    return jsonify({'game_id': game_id, 'state': GAMES[game_id]}), 201

@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = GAMES.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    return jsonify({'game_id': game_id, 'state': game})

@app.route('/games/<int:game_id>/moves', methods=['POST'])
def post_move(game_id):
    payload = request.get_json(force=True) or {}
    move_uci = payload.get('move')
    game = GAMES.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    try:
        result = apply_move(game['fen'], move_uci)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    # Update game state
    game['fen'] = result['fen']
    game['turn'] = result['turn']
    game['moves'].append({'move': move_uci, 'board': game['fen']})

    # If AI turn, compute and apply AI move
    if game['turn'] == 'b' and not result['is_game_over']:
        ai_move = ai_move_for_fen(game['fen'], depth=1)
        if ai_move:
            ai_result = apply_move(game['fen'], ai_move)
            game['fen'] = ai_result['fen']
            game['turn'] = ai_result['turn']
            game['moves'].append({'move': ai_move, 'board': game['fen']})
            result['ai_move'] = ai_move
            result['ai_result'] = ai_result

    result_state = {
        'fen': game['fen'],
        'turn': game['turn'],
        'moves': game['moves'],
        'game_over': result.get('is_game_over', False)
    }
    return jsonify(result_state)

@app.route('/games/<int:game_id>/over', methods=['GET'])
def game_over(game_id):
    game = GAMES.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    board = __import__('chess').Board(game['fen'])
    return jsonify({'game_over': board.is_game_over(), 'result': board.result() if board.is_game_over() else None})

if __name__ == '__main__':
    app.run(debug=True)
