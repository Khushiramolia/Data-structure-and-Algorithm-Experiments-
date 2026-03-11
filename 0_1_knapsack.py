def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp



def print_knapsack_table(dp, capacity):
    n = len(dp) - 1
    print("\nKnapsack DP Table:\n")
    print("     ", end="")
    for w in range(capacity + 1):
        print(f"{w:>4}", end="")
    print()

    print("     " + "----" * (capacity + 1))

    for i in range(n + 1):
        print(f"{i:>2}  |", end="")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:>4}", end="")
        print()

#backtracking
def find_selected_items(dp, weights, values, capacity):
    selected_items = []
    i = len(weights)
    w = capacity

    while i > 0 and w > 0:
        # If the value comes from the current item being included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)  # item number (1-indexed)
            w -= weights[i - 1]
        i -= 1

    selected_items.reverse()
    return selected_items


if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    weights = list(map(int, input("Enter weights of items: ").split()))
    values = list(map(int, input("Enter values of items: ").split()))
    capacity = int(input("Enter knapsack capacity: "))

    dp = knapsack(weights, values, capacity)

    print_knapsack_table(dp, capacity)

    max_profit = dp[len(weights)][capacity]
    print(f"\nMaximum Profit: {max_profit}")

    selected_items = find_selected_items(dp, weights, values, capacity)
    print("Items Selected:", selected_items)

    if selected_items:
        total_weight = sum(weights[i - 1] for i in selected_items)
        total_value = sum(values[i - 1] for i in selected_items)
        print(f"Total Weight: {total_weight}")
        print(f"Total Value: {total_value}")

#time complexity ->O(nW)
