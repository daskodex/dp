def search_insert(nums, target) -> int:
    first = 0
    last = len(nums) - 1

    index = -1

    while (first <= last) and (index == -1):
        mid = (first + last) // 2

        if nums[mid] == target:
            index = mid
        else:
            if target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if index == -1:
        index = ((first + last) // 2) + 1

    return index

if __name__ == '__main__':
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4


