def main():
    t = int(input())
    for _ in range(t):
        word = input().strip()
        # Remove os dois últimos caracteres "us" para obter a raiz
        root = word[:-2]
        # Forma plural: raiz + "i"
        print(root + "i")
        
if __name__ == "__main__":
    main()
