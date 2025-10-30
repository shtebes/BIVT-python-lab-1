def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return ValueError
    min_zn = nums[0]
    max_zn = nums[0]
    for x in nums:
        if x < min_zn:
            min_zn = x
        if x > max_zn:
            max_zn = x
    return tuple(min_zn, max_zn)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    flat_list = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            return TypeError
        for j in i:
            flat_list.append(j)
    return flat_list

print("min_max:")
print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))
print("unique_sorted:")
print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
print("flatten:")
print(flatten([[1,2],[3,4]]))
print(flatten([[1,2],(3,4,5)]))
print(flatten([[1],[],[2,3]]))
print(flatten([[1,2],"ab"]))