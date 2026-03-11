n = int(input("Enter number of items: "))

value = []
weight = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

capacity = float(input("Enter capacity of knapsack: "))

items = [(i, value[i] / weight[i], weight[i], value[i]) for i in range(n)]

items.sort(key=lambda x: x[1], reverse=True)

total_value = 0
selected_items = []  

for idx, ratio, w, v in items:
    if capacity >= w:
      
        total_value += v
        capacity -= w
        selected_items.append((idx + 1, 1))  
    else: 
        fraction = capacity / w
        total_value += v * fraction
        selected_items.append((idx + 1, fraction))
        capacity = 0
        break  


print("\nMaximum total value in knapsack =", total_value)
print("Items selected:")
for item_num, fraction in selected_items:
    if fraction == 1:
        print(f"Item {item_num}: 100% taken")
    else:
        print(f"Item {item_num}: {fraction*100:.2f}% taken")

#This is a Fractional Knapsack greedy algorithm that selects items based on the highest value-to-weight ratio to maximize total value.
#Time complexity is O(n log n) because items are sorted by ratio, and then scanned once to fill the knapsack.