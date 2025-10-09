# Лабораторная работа 2

### задание 1

``` python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return ValueError
    else:
        return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    flattened = []
    for row in mat:
        if type(row) is not list or not tuple:
            return TypeError
        else:
            for item in row:
                flattened.append(item)
    return flattened
```
![img1](/images/lab2/exA.png)

### задание 2

``` python
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

```
![img2](/images/lab2/exB.png)

# задание 3

``` python
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if not isinstance(gpa, (int, float)):
        raise TypeError
    if not fio.strip():
        raise ValueError
    if not group.strip():
        raise ValueError
    
    cleaned_fio = ' '.join(fio.split())
    parts = cleaned_fio.split()
    
    surname = parts[0].title()
    initials = '.'.join(part[0].upper() for part in parts[1:]) + '.'
    
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
```
![img3](/images/lab2/exC.png)