import random
import time

# Partition function (first element as pivot)
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[i] = arr[i], arr[low]
    return i

# Iterative QuickSort using stack
def quick_sort_iterative(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    return arr

# Test arrays
array_sizes = [10000, 50000, 100000]

for n in array_sizes:
    print(f"\n=== Results for n={n} ===")

    # Best Case: ascending
    ascending = list(range(1, n + 1))
    start = time.perf_counter()
    sorted_asc = quick_sort_iterative(ascending)
    end = time.perf_counter()
    print(f"Sorted: {sorted_asc[:15]} | Time: {end - start:.3f} sec")

    # Worst Case: descending
    descending = list(range(n, 0, -1))
    start = time.perf_counter()
    sorted_desc = quick_sort_iterative(descending)
    end = time.perf_counter()
    print(f"Reversely Sorted: {sorted_desc[:15]} | Time: {end - start:.3f} sec")

    # Average Case: random
    random_arr = random.sample(range(1, n * 10), n)
    start = time.perf_counter()
    sorted_rand = quick_sort_iterative(random_arr)
    end = time.perf_counter()
    print(f"Random: {sorted_rand[:15]} | Time: {end - start:.3f} sec")
