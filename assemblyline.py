def assembly_line_scheduling():
    n = int(input("Enter number of stations: "))

    print("Enter processing times for Line 1 (space separated): ")
    a1 = list(map(int, input().split()))

    print("Enter processing times for Line 2 (space separated): ")
    a2 = list(map(int, input().split()))

    print("Enter transfer times from Line 1 to Line 2 (space separated, n-1 values): ")
    t1 = list(map(int, input().split()))

    print("Enter transfer times from Line 2 to Line 1 (space separated, n-1 values): ")
    t2 = list(map(int, input().split()))

    e1 = int(input("Enter entry time for Line 1: "))
    e2 = int(input("Enter entry time for Line 2: "))
    x1 = int(input("Enter exit time for Line 1: "))
    x2 = int(input("Enter exit time for Line 2: "))

    # DP tables
    f1 = [0] * n
    f2 = [0] * n
    l1 = [0] * n
    l2 = [0] * n

    # Base case
    f1[0] = e1 + a1[0]
    f2[0] = e2 + a2[0]

    # DP Calculation
    for j in range(1, n):
        # Line 1
        if f1[j - 1] + a1[j] <= f2[j - 1] + t2[j - 1] + a1[j]:
            f1[j] = f1[j - 1] + a1[j]
            l1[j] = 1
        else:
            f1[j] = f2[j - 1] + t2[j - 1] + a1[j]
            l1[j] = 2

        # Line 2
        if f2[j - 1] + a2[j] <= f1[j - 1] + t1[j - 1] + a2[j]:
            f2[j] = f2[j - 1] + a2[j]
            l2[j] = 2
        else:
            f2[j] = f1[j - 1] + t1[j - 1] + a2[j]
            l2[j] = 1

    # Final comparison (exit)
    if f1[n - 1] + x1 <= f2[n - 1] + x2:
        f_star = f1[n - 1] + x1
        l_star = 1
    else:
        f_star = f2[n - 1] + x2
        l_star = 2

    print("\nMinimum total time:", f_star)
#It computes the minimum time to reach each station on both lines, deciding whether to stay on the same line or switch. At the end, it picks the line with the smaller total time including the exit.

    # ============================
    # PRINT DP TABLE
    # ============================
    print("\nDP Table for f1 (Line 1):")
    print(f1)

    print("\nDP Table for f2 (Line 2):")
    print(f2)

    print("\nDecision Table l1:")
    print(l1)

    print("\nDecision Table l2:")
    print(l2)

    # =============================
    # BACKTRACKING PATH
    # =============================
    print("\nOptimal Path:")
    line = l_star
    print(f"Line {line}, Station {n}")

    for j in range(n - 1, 0, -1):
        if line == 1:
            line = l1[j]
        else:
            line = l2[j]
        print(f"Line {line}, Station {j}")


# Run
assembly_line_scheduling()

#O(n) — because we make a constant number of decisions at each of the n stations.
