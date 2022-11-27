def quickSort(q, low, high):
    if low < high:
        pi = partition(q, low, high)
        quickSort(q, low, pi - 1)
        quickSort(q, pi, high)


def partition(q, low, high):
    i = low - 1
    pivot = q[high]
    for j in range(low, high):
        if q[j] <= pivot:
            i = i + 1
            q[i], q[j] = q[j], q[i]

    q[i + 1], q[high] = q[high], q[i + 1]
    return i + 1


if __name__ == "__main__":
    q = [3, 2, 4, 2, 6, 7]
    n = len(q)
    quickSort(q, 0, n - 1)
    print(q)
