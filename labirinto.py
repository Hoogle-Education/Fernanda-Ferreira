def caminho_diagonal(m):
    if not m or not m[0]:
        return False

    rows = len(m)
    cols = len(m[0])
    caminho = []

    def backtrack(row, col):

        # caso base - falha
        if row >= rows or col >= cols or m[row][col] == 1:
            return False

        if m[row][col] == 2:
            row_ant, _ = caminho[-1]

            if row_ant == row:
                if col+1 >= cols or m[row][col + 1] == 2:
                    return False

                para_direita = backtrack(row, col + 1)
                if para_direita:
                    return True
            else:
                if row+1 >= rows or m[row + 1][col] == 2:
                    return False

                para_baixo = backtrack(row + 1, col)
                if para_baixo:
                    return True

            return False
        else:

            caminho.append((row, col))

            # caso base - sucesso
            if row == rows-1 and col == cols-1:
                return True

            # caso recursivo - direito
            para_direita = backtrack(row, col + 1)
            if para_direita:
                return True

            # caso recursivo - baixo
            para_baixo = backtrack(row + 1, col)
            if para_baixo:
                return True

            caminho.pop()
            return False

    if backtrack(0, 0):
        return caminho
    else:
        return False


matriz = [
    [0, 1],
    [0, 0]
]

# print(caminho_diagonal(matriz))
# print(caminho_diagonal([
#     [0, 0, 1],
#     [0, 1, 0],
#     [0, 0, 0]
# ]))

labirinto1 = [[0, 0, 1], [0, 1, 0], [0, 0, 0]]
labirinto2 = [[0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 0]]
labirinto3 = [[0, 0], [1, 1]]
labirinto4 = [[2, 0], [0, 0]]
labirinto5 = [[0, 0], [0, 2]]
labirinto6 = [
    [0, 2, 0],
    [1, 0, 0]
]
labirinto7 = [
    [0, 2, 1],
    [1, 0, 0]
]
labirinto8 = [
    [0, 1, 2, 0],
    [0, 2, 2, 0]
]
labirinto9 = [
    [0, 1, 2, 0],
    [2, 2, 2, 0],
    [0, 2, 0, 0]
]


print(caminho_diagonal(labirinto6))
print(caminho_diagonal(labirinto7))
print(caminho_diagonal(labirinto8))
print(caminho_diagonal(labirinto9))
