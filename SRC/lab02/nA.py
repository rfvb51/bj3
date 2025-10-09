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

print('min_max')
print("[3, -1, 5, 5, 0] ->", min_max([3, -1, 5, 5, 0]))
print("[42] ->", min_max([42]))
print("[-5, -2 ,-9] ->", min_max([-5, -2 ,-9]))
print("[] ->", min_max([]))
print("[1.5, 2, 2.0, -3.1] ->", min_max([1.5, 2, 2.0, -3.1]))

print('unique_sorted')
print("[3, 1, 2, 1, 3] ->", unique_sorted([3, 1, 2, 1, 3]))
print("[] ->", unique_sorted([]))
print("[-1, -1, 0, 2, 2] ->", unique_sorted([-1, -1, 0, 2, 2]))
print("[1.0, 1, 2.5, 2.5, 0] ->", unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print('flatten function')
print("[[1, 2], [3, 4]] ->", flatten([[1, 2], [3, 4]]))
print("[[1, 2], (3, 4, 5)] ->", flatten([[1, 2], (3, 4, 5)]))
print("[[1], [], [2, 3]] ->", flatten([[1], [], [2, 3]]))
print(f"[[1, 2], 'ab'] ->", flatten([[1, 2], "ab"]))