import chess

# Simple material evaluation for a chess board
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000,
}


def _evaluate_board(board: chess.Board) -> int:
    # Positive score favors White; negative favors Black
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = PIECE_VALUES[piece.piece_type]
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
    return score


def _minimax(board: chess.Board, depth: int, alpha: int, beta: int, maximizing: bool):
    if depth == 0 or board.is_game_over():
        return _evaluate_board(board), None

    best_move = None
    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = _minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = _minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def ai_move_for_fen(fen: str, depth: int = 1) -> str | None:
    """Return the best move in UCI format for the side to move on the given FEN.
    depth controls the search depth (1-3 recommended for MVP).
    """
    board = chess.Board(fen)
    if board.is_game_over():
        return None
    # Clamp depth to reasonable values to keep MVP responsive
    depth = max(1, min(depth, 3))
    _, best_move = _minimax(board, depth, -float('inf'), float('inf'), True)
    if best_move is None:
        # If minimax couldn't find a move (shouldn't happen in normal positions)
        # fall back to the first legal move
        try:
            best_move = next(iter(board.legal_moves))
        except StopIteration:
            return None
    return best_move.uci()
