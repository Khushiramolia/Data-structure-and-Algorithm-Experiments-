import random
import time
import matplotlib.pyplot as plt

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Function to measure execution time
def measure_time(arr):
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    return end - start

# Input sizes (fixed)
sizes = [10000, 50000, 100000]

# Store results
random_times = []
ascending_times = []
descending_times = []

# Run tests
for size in sizes:
    # Random input
    arr_random = [random.randint(1, size) for _ in range(size)]
    t_random = measure_time(arr_random[:])
    random_times.append(t_random)

    # Ascending input
    arr_sorted = list(range(size))
    t_ascending = measure_time(arr_sorted[:])
    ascending_times.append(t_ascending)

    # Descending input
    arr_desc = list(range(size, 0, -1))
    t_desc = measure_time(arr_desc[:])
    descending_times.append(t_desc)

# Print execution times
print("\nExecution Times for Bubble Sort (in seconds):")
for i, size in enumerate(sizes):
    print(f"Size {size}: Random = {random_times[i]:.4f}, Ascending = {ascending_times[i]:.4f}, Descending = {descending_times[i]:.4f}")

# Plot bar graph
bar_width = 0.25
positions1 = range(len(sizes))
positions2 = [p + bar_width for p in positions1]
positions3 = [p + bar_width for p in positions2]

plt.bar(positions1, random_times, width=bar_width, label="Random")
plt.bar(positions2, ascending_times, width=bar_width, label="Ascending")
plt.bar(positions3, descending_times, width=bar_width, label="Descending")

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Bubble Sort Performance (10k, 50k, 100k elements)")
plt.xticks([p + bar_width for p in positions1], ["10k", "50k", "100k"])
plt.legend()
plt.show()


#time complexity -—>buble sort 
#Best case → O(n)
#Average case → O(n²)
#Worst case → O(n²)

