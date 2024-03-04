def find_word(board, word, visited, x, y, result):
    if word in dictionary:
        result.add(word)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
            visited[nx][ny] = True
            find_word(board, word + board[nx][ny], visited, nx, ny, result)
            visited[nx][ny] = False

def find_all_words(board):
    result = set()
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            visited = [[False] * cols for _ in range(rows)]
            visited[i][j] = True
            find_word(board, board[i][j], visited, i, j, result)
    return result

board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

dictionary = {'START', 'NOTE', 'SAND', 'STONED'}

print(find_all_words(board))
