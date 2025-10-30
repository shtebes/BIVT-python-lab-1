def check_rectangular(mat: list[list[float | int]]) -> bool:
    if not mat:
        return True
    len_row_1 = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != len_row_1:
            return False
    return True

def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    if check_rectangular(mat) == False:
        return "ValueError"
    trans_mat = []
    for j in range (len(mat[0])):
        trans_row = []
        for i in range(len(mat)):
            trans_row.append(mat[i][j])
        trans_mat.append(trans_row)
    return trans_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if check_rectangular(mat) == False:
        return "ValueError"
    sum_row = []
    for row in mat:
        sum_row.appen(sum(row))
    return sum_row

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if check_rectangular(mat) == False:
        return "ValueError"
    return row_sums(transpose(mat))

print("transpose:")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print("row_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print("col_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
