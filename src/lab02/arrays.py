def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError()
    min_v = nums[0]
    max_v = nums[0]
    for x in nums[1:]:
        if x < min_v:
            min_v = x
        if x > max_v:
            max_v = x
    return min_v, max_v

def unique_sorted(nums: list[float | int]) -> list[float | int]:\
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    flat_list = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError()
        flat_list.extend(i)
    return flat_list