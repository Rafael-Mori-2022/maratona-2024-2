def main():
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        stones = list(map(int, input().split()))
        
        min_val = min(stones)
        max_val = max(stones)
        idx_min = stones.index(min_val)
        idx_max = stones.index(max_val)
        
        # Estratégia 1: remover os stones do início até que ambos sejam removidos.
        # O número de movimentos é o índice máximo entre os dois, mais 1 (por conta do 0-index).
        option1 = max(idx_min, idx_max) + 1
        
        # Estratégia 2: remover os stones do final até que ambos sejam removidos.
        # Para um stone na posição i, os movimentos necessários a partir do final são n - i.
        option2 = max(n - idx_min, n - idx_max)
        
        # Estratégia 3: remover alguns stones do início e outros do final.
        # É necessário remover do início até o stone que estiver mais à esquerda entre os dois,
        # e do final até o stone que estiver mais à direita.
        option3 = (min(idx_min, idx_max) + 1) + (n - max(idx_min, idx_max))
        
        print(min(option1, option2, option3))
        
if __name__ == "__main__":
    main()
