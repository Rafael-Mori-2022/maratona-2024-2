def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        k = 0
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                k += 1
            else:
                break
        
        print(n - 2 * k)
        
if __name__ == "__main__":
    main()
