import pytest
import chess
from backend.engine import create_initial_state, apply_move


def test_initial_state_fen():
    state = create_initial_state()
    assert 'fen' in state
    assert isinstance(state['fen'], str)
    assert state['fen'] == chess.STARTING_FEN


def test_apply_valid_move_updates_fen():
    init = create_initial_state()
    new_state = apply_move(init['fen'], 'e2e4')
    assert 'fen' in new_state
    assert new_state['fen'] != init['fen']
    # Ensure the move is reflected on the board by comparing piece placement
    board_before = chess.Board(init['fen'])
    board_after = chess.Board(new_state['fen'])
    assert board_before.piece_at(chess.E2) is not None
    assert board_after.piece_at(chess.E4) is not None
