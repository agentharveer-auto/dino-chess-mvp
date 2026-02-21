import chess
from backend.engine import create_initial_state, apply_move
from backend.ai import ai_move_for_fen


def test_ai_move_after_white_move_is_legal():
    init = create_initial_state()
    after_white = apply_move(init['fen'], 'e2e4')
    # AI should move as Black on its turn; request a move for the current board
    move = ai_move_for_fen(after_white['fen'], depth=1)
    assert move is None or isinstance(move, str)
    if move:
        board = chess.Board(after_white['fen'])
        m = chess.Move.from_uci(move)
        assert m in board.legal_moves
