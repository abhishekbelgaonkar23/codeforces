matrix = []

for i in range(5):
    matrix.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if matrix [i][j] == 1:
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            break
