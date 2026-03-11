def greedy_change(coins, amount):
    coins.sort(reverse=True)
    count_map = {c: 0 for c in coins}  # Creates a dictionary to store how many times each coin is used.

    for c in coins: #Loops through each coin value, starting from the largest.
        while amount >= c: #While the current coin can still be used without exceeding the remaining amount…
            amount -= c #Subtracts the coin’s value from the total amount.
            count_map[c] += 1 #Increases the count of that coin in the dictionary.

    if amount != 0:
        return None
    return count_map

coins = list(map(int, input("Enter coin denominations: ").split())) #Takes user input for coins and converts them into a list of integers.
amount = int(input("Enter amount: "))

change = greedy_change(coins, amount)

if change:
    print("\nCoins used (per denomination):")
    total = 0
    for c in sorted(change.keys(), reverse=True):
        print(f"{c}: {change[c]}")
        total += change[c]
    print(f"\nTotal number of coins: {total}")
else:
    print("Not possible")

#Time complexity: O(n + k)
#where n is the number of coin types and k is the number of coins used in the loop.
#In short: The code greedily picks the biggest coin that fits the amount and repeats until the amount becomes zero.