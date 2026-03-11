import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1   
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key

sizes = [10000, 50000, 100000]
results = {"Random": [], "Increasing": [], "Decreasing": []}

for n in sizes:
    arr = [random.randint(1, n) for _ in range(n)]
    start = time.time()
    insertion_sort(arr)
    results["Random"].append(time.time() - start)


    arr = list(range(n))
    start = time.time()
    insertion_sort(arr)
    results["Increasing"].append(time.time() - start)


    arr = list(range(n, 0, -1))
    start = time.time()
    insertion_sort(arr)
    results["Decreasing"].append(time.time() - start)

print("Random:", results["Random"])
print("Increasing:", results["Increasing"])
print("Decreasing:", results["Decreasing"])

x = range(len(sizes))
bar_width = 0.25

plt.bar([p - bar_width for p in x], results["Random"], width=bar_width, label="Random")
plt.bar(x, results["Increasing"], width=bar_width, label="Increasing")
plt.bar([p + bar_width for p in x], results["Decreasing"], width=bar_width, label="Decreasing")

plt.xticks(x, [f"{s}" for s in sizes])
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Insertion Sort Performance (10k, 50k, 100k)")
plt.legend()
plt.show()


#Insertion Sort shifts elements to insert each item in its correct position, with best-case time O(n), average and worst-case time O(n²), and space complexity O(1).
#The graph shows that Insertion Sort is much slower on random and descending arrays, while it is fastest on already sorted (increasing) arrays. 
#Execution time increases drastically with input size, especially for reverse-sorted data.