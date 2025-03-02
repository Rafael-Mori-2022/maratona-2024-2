def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        robin = 0
        counter = 0

        a_list = list(map(int, input().split()))
        
        for a in a_list:
            if a >= k:
                robin += a
            elif a == 0 and robin > 0:
                robin -= 1
                counter += 1
        
        print(counter)


if __name__ == "__main__":
    main()
