def main():
    n = int(input().strip())
    v = list(map(int, input().split()))
    
    # Preprocessa prefix sum do array original
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + v[i]
    
    # Ordena o array para responder às queries do tipo 2
    sorted_v = sorted(v)
    prefix_sorted = [0] * (n + 1)
    for i in range(n):
        prefix_sorted[i + 1] = prefix_sorted[i] + sorted_v[i]
    
    m = int(input().strip())
    for _ in range(m):
        typ, l, r = map(int, input().split())
        if typ == 1:
            # Query do tipo 1: soma do segmento [l, r] no array original
            print(prefix[r] - prefix[l - 1])
        else:
            # Query do tipo 2: soma do segmento [l, r] no array ordenado (não decrescente)
            print(prefix_sorted[r] - prefix_sorted[l - 1])

if __name__ == "__main__":
    main()
