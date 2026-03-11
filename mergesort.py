import random
import time
import matplotlib.pyplot as plt

# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def random_array(n):
    return [random.randint(1, 10000) for _ in range(n)]

def sorted_array(n):
    return list(range(1, n + 1))

def reverse_sorted_array(n):
    return list(range(n, 0, -1))

# Measure execution time
def measure_time(input_generator, sizes):
    times = []
    for n in sizes:
        arr = input_generator(n)
        start = time.time()
        _ = merge_sort(arr)
        end = time.time()
        elapsed = round(end - start, 2)
        times.append(elapsed)
        print(f"Merge sorted {n} elements in {elapsed:.2f} seconds")
    return times

# Sizes for testing
sizes = [10000, 50000, 100000]

# Measure times
time_random = measure_time(random_array, sizes)
time_sorted = measure_time(sorted_array, sizes)
time_reverse = measure_time(reverse_sorted_array, sizes)

# Print table (manually)
print("\nExecution Time Table (seconds):")
print(f"{'Input Size':<12}{'Random':<12}{'Ascending':<12}{'Descending':<12}")
for i in range(len(sizes)):
    print(f"{sizes[i]:<12}{time_random[i]:<12}{time_sorted[i]:<12}{time_reverse[i]:<12}")

# Plot bar chart
bar_width = 0.25
x = range(len(sizes))

plt.bar([p - bar_width for p in x], time_random, width=bar_width, label='Random')
plt.bar(x, time_sorted, width=bar_width, label='Ascending')
plt.bar([p + bar_width for p in x], time_reverse, width=bar_width, label='Descending')

plt.xticks(x, ["10k", "50k", "100k"])
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Merge Sort Performance")
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()
#The graph shows that Merge Sort’s execution time increases steadily with input size, confirming its O(n log n) time complexity.
#The random dataset takes slightly more time than sorted and reverse inputs due to extra comparisons during the merge process.
