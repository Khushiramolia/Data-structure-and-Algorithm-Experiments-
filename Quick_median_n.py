import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    first, middle, last = arr[0], arr[len(arr)//2], arr[-1]
    pivot = sorted([first, middle, last])[1]  # median-of-three

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


for n in [10000, 50000, 100000]:
    print(f"\n=== Results for n={n} ===")

    increasing = list(range(1, n + 1))
    start = time.perf_counter()
    sorted_inc = quick_sort(increasing)
    end = time.perf_counter()
    print(f"Best Case (Sorted): {sorted_inc[:15]} | Time: {end - start:.3f} sec")

    decreasing = list(range(n, 0, -1))
    start = time.perf_counter()
    sorted_dec = quick_sort(decreasing)
    end = time.perf_counter()
    print(f"Worst Case (Reversed): {sorted_dec[:15]} | Time: {end - start:.3f} sec")

    random_order = random.sample(range(1, n + 1), n)
    start = time.perf_counter()
    sorted_rand = quick_sort(random_order)
    end = time.perf_counter()
    print(f"Average Case (Random): {sorted_rand[:15]} | Time: {end - start:.3f} sec\n")
