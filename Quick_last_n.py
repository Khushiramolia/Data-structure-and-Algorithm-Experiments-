import random
import time


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))   
            stack.append((pi + 1, high))  
    return arr



array_sizes = [10000, 50000, 100000]

for n in array_sizes:
    print(f"\n=== Results for n={n} ===")

    
    ascending = list(range(1, n + 1))
    start = time.perf_counter()
    sorted_asc = quick_sort_iterative(ascending)
    end = time.perf_counter()
    print(f"Sorted: {sorted_asc[:15]} | Time: {end - start:.3f} sec")

   
    descending = list(range(n, 0, -1))
    start = time.perf_counter()
    sorted_desc = quick_sort_iterative(descending)
    end = time.perf_counter()
    print(f"Reversely Sorted: {sorted_desc[:15]} | Time: {end - start:.3f} sec")

   
    random_order = random.sample(range(1, n * 10), n)
    start = time.perf_counter()
    sorted_rand = quick_sort_iterative(random_order)
    end = time.perf_counter()
    print(f"Random: {sorted_rand[:15]} | Time: {end - start:.3f} sec") 