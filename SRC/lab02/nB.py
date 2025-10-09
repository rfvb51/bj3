def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            return ValueError
        
    result = []
    for col_idx in range(len(mat[0])):
        new_row = []
        for row_idx in range(len(mat)):
            new_row.append(mat[row_idx][col_idx])
        result.append(new_row)
    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            return ValueError
        
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            return ValueError
        
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(rowlenght)]  

print('transpose')
print("[[1, 2, 3]] ->", transpose([[1, 2, 3]]))
print("[[1], [2], [3]] ->", transpose([[1], [2], [3]]))
print("[[1, 2], [3, 4]] ->", transpose([[1, 2], [3, 4]]))
print("[] ->", transpose([]))
print("[[1, 2], [3]] ->", transpose([[1, 2], [3]]))

print('row_sums')
print('[[1, 2, 3], [4, 5, 6]] ->', row_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]] ->', row_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] ->', row_sums([[0, 0], [0, 0]]))
print('[[1, 2], [3]] ->', row_sums([[1, 2], [3]]))

print('col_sums')
print('[[1, 2, 3], [4, 5, 6]] ->', col_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]] ->', col_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] ->', col_sums([[0, 0], [0, 0]]))
print('[[1, 2], [3]] ->', col_sums([[1, 2], [3]]))