
def merge_sort(nums):
    i = 1
    tmp = [0] * len(nums)
    while i < len(nums):
        low = 0
        while low < len(nums):
            mid = low + i
            high = min(low + 2 * i, len(nums))
            if mid < high:
                merge(nums, low, mid, high, tmp)
            low += 2 * i
        i *= 2


def merge(nums, low, mid, high, tmp):
    i = low
    j = mid
    k = low
    while i < mid and j <= high:
        if nums[i] < nums[j]:
            tmp[k] = nums[i]
            k += 1
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
            k += 1
    if i < mid:
        tmp[k:high + 1] = nums[i:mid]
    if j <= high:
        tmp[k:high + 1] = nums[j:high + 1]
    nums[low:high + 1] = tmp[low:high + 1]


def main():
    nums = [eval(x) for x in input().split()]
    merge_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
