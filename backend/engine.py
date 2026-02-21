import chess

"""
High-level game state helpers using python-chess for standard chess rules.
"""


def create_initial_state():
    board = chess.Board()
    return {
        "fen": board.fen(),
        "turn": "w",
        "is_game_over": board.is_game_over(),
        "result": board.result() if board.is_game_over() else None,
    }


def apply_move(state_fen, move_uci):
    """Apply a move (in UCI format) to the given FEN state and return the new state."""
    board = chess.Board(state_fen)
    move = chess.Move.from_uci(move_uci)
    if move not in board.legal_moves:
        raise ValueError("Illegal move: {} for position {}".format(move_uci, state_fen))
    board.push(move)
    return {
        "fen": board.fen(),
        "turn": "w" if board.turn else "b",
        "is_game_over": board.is_game_over(),
        "result": board.result() if board.is_game_over() else None,
    }
