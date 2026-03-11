import time
import random
import matplotlib.pyplot as plt

# Selection Sort function
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Function to test performance
def measure_time(arr):
    start = time.time()
    selection_sort(arr)
    end = time.time()
    return end - start

# Input sizes
sizes = [10000, 50000, 100000]

# To store results
random_times = []
increasing_times = []
decreasing_times = []

for size in sizes:
    # Random input
    arr_random = [random.randint(1, size) for _ in range(size)]
    random_times.append(measure_time(arr_random.copy()))

    # Increasing input
    arr_inc = list(range(size))
    increasing_times.append(measure_time(arr_inc.copy()))

    # Decreasing input
    arr_dec = list(range(size, 0, -1))
    decreasing_times.append(measure_time(arr_dec.copy()))

# Plotting bar graph
bar_width = 0.25
positions1 = range(len(sizes))
positions2 = [p + bar_width for p in positions1]
positions3 = [p + bar_width for p in positions2]

plt.bar(positions1, random_times, width=bar_width, label="Random")
plt.bar(positions2, increasing_times, width=bar_width, label="Increasing")
plt.bar(positions3, decreasing_times, width=bar_width, label="Decreasing")

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Selection Sort Performance (10k, 50k, 100k)")
plt.xticks([p + bar_width for p in positions1], ["10k", "50k", "100k"])
plt.legend()
plt.show()

#—>selection sort
#Best case → O(n²)
#Average case → O(n²)
#Worst case → O(n²)
#The graph shows that the execution time increases very rapidly as the input size increases, confirming Selection Sort’s O(n²) time complexity. 
##It also shows almost no difference between random, increasing, and decreasing inputs because Selection Sort always performs the same number of comparisons regardless of the initial order.
