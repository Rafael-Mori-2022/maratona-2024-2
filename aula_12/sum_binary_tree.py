def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        total = 0
        # Enquanto n for positivo, some o valor e passe para o pai (n // 2)
        while n:
            total += n
            n //= 2
        print(total)

if __name__ == "__main__":
    main()
