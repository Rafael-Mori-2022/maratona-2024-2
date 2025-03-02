def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        
        # Conta o número de células brancas ('W') no primeiro segmento de tamanho k.
        white_count = s[:k].count('W')
        ans = white_count
        
        # Percorre os segmentos de tamanho k usando janela deslizante.
        for i in range(1, n - k + 1):
            # Remove o efeito do caractere que saiu da janela
            if s[i - 1] == 'W':
                white_count -= 1
            # Adiciona o novo caractere que entrou na janela
            if s[i + k - 1] == 'W':
                white_count += 1
            ans = min(ans, white_count)
            
        print(ans)

if __name__ == "__main__":
    main()
