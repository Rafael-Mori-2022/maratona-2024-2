def main():
    n = int(input())
    total = n * (n + 1) // 2
    # A partition is possible if and only if total sum is even.
    if total % 2 != 0:
        print("NO")
        return

    print("YES")
    half = total // 2
    set1 = []
    set2 = []

    # Greedily assign numbers from n down to 1.
    for i in range(n, 0, -1):
        if half >= i:
            set1.append(i)
            half -= i
        else:
            set2.append(i)
    
    # It's allowed to print any valid partition.
    # Optionally, sort each set in increasing order before printing.
    set1.sort()
    set2.sort()
    
    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))

if __name__ == "__main__":
    main()
