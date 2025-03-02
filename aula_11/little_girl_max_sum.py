def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Usaremos a técnica do array de diferença para contar quantas vezes cada índice é consultado.
    freq = [0] * (n + 1)
    for _ in range(q):
        l, r = map(int, input().split())
        freq[l - 1] += 1
        freq[r] -= 1  # r é inclusivo, então diminuímos a partir do índice r (0-indexed)
    
    # Calcula os prefix sums para obter a frequência de cada posição.
    for i in range(1, n):
        freq[i] += freq[i - 1]
    freq = freq[:n]  # Desconsidera o último elemento extra
    
    # Ordena o array e as frequências em ordem decrescente.
    arr.sort(reverse=True)
    freq.sort(reverse=True)
    
    # Atribui os maiores valores aos índices mais "consultados"
    res = 0
    for a, f in zip(arr, freq):
        res += a * f
        
    print(res)

if __name__ == "__main__":
    main()
