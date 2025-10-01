def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    kol_1 = len(mat[0])
    for line in enumerate(mat):
        if len(line) != kol_1:
            raise ValueError()
    trans_mat = []
    for j in range (len(mat[0])):
        new_line = []
        for i in range(len(mat)):
            new_line.append(mat[i][j])
        trans_mat.append(new_line)
    return trans_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    kol_1 = len(mat[0])
    for line in enumerate(mat):
        if len(line) != kol_1:
            raise ValueError()
    summa = []
    for line in mat:
        summa.append(float(sum(line)))
    return summa

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    kol_1 = len(mat[0])
    for line in enumerate(mat):
        if len(line) != kol_1:
            raise ValueError()
    summa = []
    for j in range(len(mat[0])):
        col_sum = sum(mat[i][j] for i in range (len(mat)))
        summa.append(float(col_sum))
    return summa

    