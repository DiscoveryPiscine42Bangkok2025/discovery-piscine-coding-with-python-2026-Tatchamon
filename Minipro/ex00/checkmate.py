def checkmate(board):
    try:
        if not board:
            print("Fail")
            return

        rows = board.splitlines()
        size = len(rows)

        # Board must be square
        if any(len(row) != size for row in rows):
            print("Error")
            return

        # Locate King
        king_pos = None
        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    break
            if king_pos:
                break

        if not king_pos:
            print("Fail")
            return

        kr, kc = king_pos

        def in_bounds(r, c):
            return 0 <= r < size and 0 <= c < size

        # Check Pawn attacks (pawns attack downward)
        for dc in (-1, 1):
            r = kr + 1
            c = kc + dc
            if in_bounds(r, c) and rows[r][c] == 'P':
                print("Success")
                return

        # Directions for Rook / Queen
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Directions for Bishop / Queen
        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Check straight lines (Rook / Queen)
        for dr, dc in straight_dirs:
            r, c = kr + dr, kc + dc
            while in_bounds(r, c):
                piece = rows[r][c]
                if piece != '.':
                    if piece in ('R', 'Q'):
                        print("Success")
                        return
                    break
                r += dr
                c += dc

        # Check diagonals (Bishop / Queen)
        for dr, dc in diag_dirs:
            r, c = kr + dr, kc + dc
            while in_bounds(r, c):
                piece = rows[r][c]
                if piece != '.':
                    if piece in ('B', 'Q'):
                        print("Success")
                        return
                    break
                r += dr
                c += dc

        print("Fail")

    except Exception:
        # Undefined behavior → return control safely
        print("Fail")

    
