dictionary = ["START", "NOTE", "SAND", 'STONED']
M = 4
N = 4

def isWord(Str):
    return Str in dictionary

# Define eight directions: North, West, South, East, North-East, North-West, South-East, South-West
directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def findWordsUtil(boggle, visited, i, j, Str, depth):
    if isWord(Str):
        print(Str)
    if depth <= 0:
        return
    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if 0 <= new_i < M and 0 <= new_j < N and not visited[new_i][new_j]:
            findWordsUtil(boggle, visited, new_i, new_j, Str + boggle[new_i][new_j], depth - 1)

    visited[i][j] = False

def findWords(boggle):
    visited = [[False for _ in range(N)] for _ in range(M)]

    for depth in range(1, M * N + 1):  # Maximum depth set to M * N
        for i in range(M):
            for j in range(N):
                findWordsUtil(boggle, visited, i, j, boggle[i][j], depth)

boggle = [
    ["M", "S", "E", "F"],
    ["R", "A", "T", "D"],
    ["L", "O", "N", "E"],
    ["K", "A", "F", "B"]
]

print("Following words of dictionary are present:")
findWords(boggle)
