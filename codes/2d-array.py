def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = len(board)
    cols = len(board[0])
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(rows):
        for col in range(cols):
            live_n = 0
            for n in neighbours:
                r = row + n[0]
                c = col + n[1]
                if (r >= 0 and r < rows) and (c >= 0 and c < cols) and board[r][c] >= 1:
                    live_n = live_n + 1
            if (board[row][col] <= 0) and (live_n == 3):
                board[row][col] = -1
            if (board[row][col] >= 1) and (live_n < 2 or live_n > 3):
                board[row][col] = 2

    print(board)
    board = [[v%2 for v in r] for r in board]
    print(board)


gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])
