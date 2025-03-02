def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        
        # Obtém os índices das células pretas.
        black_positions = [i for i, ch in enumerate(s) if ch == 'B']
        if not black_positions:
            print(0)
            continue
        
        ops = 0
        i = 0
        while i < len(black_positions):
            # Para o primeiro índice de 'B' não coberto, digamos pos = black_positions[i]
            pos = black_positions[i]
            # Se pos está antes do último segmento possível, podemos iniciar o segmento em pos;
            # caso contrário, devemos iniciar em n-k (única opção que cubra pos)
            if pos <= n - k:
                j = pos
            else:
                j = n - k
            cover_right = j + k - 1  # o segmento cobre de j até j+k-1
            ops += 1
            # Pula todas as posições de 'B' que estão cobertas pelo segmento
            while i < len(black_positions) and black_positions[i] <= cover_right:
                i += 1
        
        print(ops)

if __name__ == "__main__":
    main()
