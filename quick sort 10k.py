import time
import random
import matplotlib.pyplot as plt
import sys

# Increase recursion limit (needed for large arrays in Quick Sort worst case)
sys.setrecursionlimit(200000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(arr):
    start = time.time()
    quick_sort(arr)
    end = time.time()
    return end - start

sizes = [10000, 50000, 100000]

random_times = []
increasing_times = []
decreasing_times = []

for size in sizes:
    arr_random = [random.randint(1, size) for _ in range(size)]
    random_times.append(measure_time(arr_random.copy()))

    arr_inc = list(range(size))
    increasing_times.append(measure_time(arr_inc.copy()))

    arr_dec = list(range(size, 0, -1))
    decreasing_times.append(measure_time(arr_dec.copy()))

bar_width = 0.25
positions1 = range(len(sizes))
positions2 = [p + bar_width for p in positions1]
positions3 = [p + bar_width for p in positions2]

plt.bar(positions1, random_times, width=bar_width, label="Random")
plt.bar(positions2, increasing_times, width=bar_width, label="Increasing")
plt.bar(positions3, decreasing_times, width=bar_width, label="Decreasing")

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Quick Sort Performance (10k, 50k, 100k)")
plt.xticks([p + bar_width for p in positions1], ["10k", "50k", "100k"])
plt.legend()
plt.show()


#quick sort
#Best Case – O(n log n)
#Happens when the pivot divides the array into two almost equal halves at every step.
#Average Case – O(n log n)
#For random data, this is what happens most of the time.
#Worst Case – O(n²)
#Happens when the pivot creates extremely unbalanced partitions.

#The graph for Quick Sort shows that execution time increases gradually as the input size increases, 
# which confirms its O(n log n) behavior in practice. It also shows almost no difference between random, 
# increasing and decreasing inputs because selecting the middle element as the pivot keeps the partitions balanced and prevents the usual worst-case slowdown.