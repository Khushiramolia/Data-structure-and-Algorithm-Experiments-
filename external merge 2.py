import random
import time
import heapq
import matplotlib.pyplot as plt


# External Merge Sort (Simulated)

def external_merge_sort(arr, chunk_size=5000):
    """Simulated external merge sort: split into chunks, sort, then merge."""
    # Step 1: Break array into chunks
    chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]
    
    # Step 2: Sort each chunk (like in-memory sorting of blocks)
    sorted_chunks = [sorted(chunk) for chunk in chunks]
    
    # Step 3: Merge chunks using heapq.merge (efficient k-way merge)
    result = list(heapq.merge(*sorted_chunks))
    return result

# Input Generators

def random_array(n):
    return [random.randint(1, 100000) for _ in range(n)]

def sorted_array(n):
    return list(range(1, n + 1))

def reverse_sorted_array(n):
    return list(range(n, 0, -1))

# Measure Execution Time
def measure_time(func, input_generator, sizes):
    times = []
    for n in sizes:
        arr = input_generator(n)
        start = time.time()
        _ = func(arr)
        end = time.time()
        elapsed = round(end - start, 2)
        times.append(elapsed)
        print(f"{func.__name__} sorted {n} elements in {elapsed:.2f} seconds")
    return times


# Sizes for Testing
sizes = [10000, 50000, 100000]

# Measure for external merge sort
time_random = measure_time(external_merge_sort, random_array, sizes)
time_sorted = measure_time(external_merge_sort, sorted_array, sizes)
time_reverse = measure_time(external_merge_sort, reverse_sorted_array, sizes)


# Print Results Table
print("\nExecution Time Table (seconds):")
print(f"{'Input Size':<12}{'Random':<12}{'Ascending':<12}{'Descending':<12}")
for i in range(len(sizes)):
    print(f"{sizes[i]:<12}{time_random[i]:<12}{time_sorted[i]:<12}{time_reverse[i]:<12}")


# Plot Bar Chart
bar_width = 0.25
x = range(len(sizes))

plt.bar([p - bar_width for p in x], time_random, width=bar_width, label='Random')
plt.bar(x, time_sorted, width=bar_width, label='Ascending')
plt.bar([p + bar_width for p in x], time_reverse, width=bar_width, label='Descending')

plt.xticks(x, ["10k", "50k", "100k"])
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("External Merge Sort Performance")
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#External Merge Sort works in two phases: sorting chunks and then merging them, and both together give an overall time complexity of O(n log n).
#The graph shows the time increases steadily with data size, and random data takes slightly longer due to more comparisons during sorting and merging.
#O(N log N)