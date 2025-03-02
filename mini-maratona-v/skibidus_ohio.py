def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        # Verifica se s possui um par de caracteres consecutivos iguais.
        has_pair = any(s[i] == s[i+1] for i in range(len(s) - 1))
        if has_pair:
            print(1)
        else:
            print(len(s))

if __name__ == "__main__":
    main()
