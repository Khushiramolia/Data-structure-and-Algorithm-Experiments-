def lcs_tables(X, Y):
   
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)] #table stores LCS lengths, initialized to 0.
    D = [[" "] * (n + 1) for _ in range(m + 1)] #table stores direction  to help backtrank 

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                D[i][j] = "↖"
            elif L[i - 1][j] >= L[i][j - 1]:
                L[i][j] = L[i - 1][j]
                D[i][j] = "↑"
            else:
                L[i][j] = L[i][j - 1]
                D[i][j] = "←"
    return L, D


def backtrack_lcs(D, X, Y):
    
    i, j = len(X), len(Y)
    lcs = []
    while i > 0 and j > 0:
        if D[i][j] == "↖":
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif D[i][j] == "↑":
            i -= 1
        else:
            j -= 1
    lcs.reverse()
    return ''.join(lcs)


def print_table(title, table, X, Y):
    
    col_width = 5
    print(f"\n{title}")
    print(" " * (col_width - 1), end="")

    # Print Y header row
    for ch in " " + Y:
        print(f"{ch:^{col_width}}", end="")
    print()

    # Print each row
    for i, row in enumerate(table):
        if i == 0:
            print(f"{' ':<{col_width-1}}", end="")
        else:
            print(f"{X[i-1]:<{col_width-1}}", end="")
        for val in row:
            print(f"{str(val):^{col_width}}", end="")
        print()


if __name__ == "__main__":
    X = input("Enter first sequence (X): ").strip()
    Y = input("Enter second sequence (Y): ").strip()

    L, D = lcs_tables(X, Y)
    lcs_result = backtrack_lcs(D, X, Y)
    lcs_length = L[len(X)][len(Y)]

    print_table("LCS Length Table (values)", L, X, Y)
    print_table("LCS Direction Table (arrows)", D, X, Y)

    print(f"\nLength of LCS: {lcs_length}")
    print(f"LCS: {lcs_result}")

#Time Complexity=O(m×n)​


