import sys

def matrix_chain_order(p): #Function to calculate minimum cost of multiplying matrices.
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for L in range(2, n + 1):  # L = chain length
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1] #This line calculates the total multiplication cost for that split:cost of left side + cost of right side + cost of multiplying the two results.
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1
    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j] - 1)
        print_optimal_parens(s, s[i][j], j)
        print(")", end="") #This function uses recursion to add brackets in the best way stored in the s table and prints the final order like:


def display_table(table, name):
    n = len(table)
    print(f"\n{name} Table:")
    print(" " * 6, end="")
    for col in range(1, n + 1):
        print(f"{col:^10}", end="")
    print("\n" + "-" * (12 * (n + 1)))

    for i in range(n, 0, -1):  # Print from bottom (n) to top (1)
        print(f"{i:<3} |", end=" ")
        for j in range(1, n + 1):
            if j < i:
                print(f"{' ':^10}", end="") #Keeps upper triangle blank for neat display.
            else:
                val = table[i-1][j-1]
                if val == 0:
                    print(f"{'0':^10}", end="")
                else:
                    print(f"{val:^10}", end="")
        print()
    print("-" * (12 * (n + 1)))


if __name__ == "__main__":
    n = int(input("Enter number of matrices: "))
    print("Enter dimensions (example: for A1(10x20), A2(20x30), enter 10 20 30):")
    p = list(map(int, input().split()))

    if len(p) != n + 1:
        print("\nError: Number of dimensions must be n+1 (since n matrices).")
        sys.exit()

    m, s = matrix_chain_order(p)

    display_table(m, "Cost (m[i][j])")
    display_table(s, "Split (s[i][j])")

    print("\nMinimum number of scalar multiplications:", m[0][n - 1])
    print("Optimal Parenthesization:", end=" ")
    print_optimal_parens(s, 0, n - 1)
    print() 

#Time Complexity ->O(n³) -> Because there are three loops: L, i, and k.

#SIMPLEST CODE-

import sys

def matrix_chain(p):
    n = len(p) - 1
    dp = [[0]*n for _ in range(n)]

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]


n = int(input("Enter number of matrices: "))
p = list(map(int, input("Enter dimensions: ").split()))

print("Minimum multiplications =", matrix_chain(p))
