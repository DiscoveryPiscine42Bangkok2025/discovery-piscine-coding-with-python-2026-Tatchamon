def checkmate(board):
        if not board:
            print("Fail")
            return
        rows = board.splitlines()
        size = len(rows)

        if any(len(row) != size for row in rows):
            print("ขนาดกระดานไม่ถูกต้อง")
            return
        king_pos = None

        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    break
            if king_pos:
                break

        if not king_pos:
            print("ไม่พบKingในกระดาน")
            return
        kr, kc = king_pos

        def in_bounds(r, c):
            return 0 <= r < size and 0 <= c < size

        for dc in (-1, 1):
            r = kr + 1
            c = kc + dc
            if in_bounds(r, c) and rows[r][c] == 'P':
                print("Success")
                return
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

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

    
