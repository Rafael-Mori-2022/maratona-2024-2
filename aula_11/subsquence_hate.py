def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        
        cost_all_zeros = s.count('1')
        cost_all_ones  = s.count('0')
        
        # Vamos construir arrays de prefixo para contar quantos '1's e '0's há até cada posição.
        prefix_ones = [0] * (n + 1)
        prefix_zeros = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i+1] = prefix_ones[i] + (1 if s[i] == '1' else 0)
            prefix_zeros[i+1] = prefix_zeros[i] + (1 if s[i] == '0' else 0)
        
        min_cost = min(cost_all_zeros, cost_all_ones)
        
        # Candidata 3: prefixo de '0's e sufixo de '1's.
        # Para uma partição em i (0 ≤ i ≤ n):
        # - s[0:i] deve ser '0' → custo = número de '1's em s[0:i] = prefix_ones[i]
        # - s[i:n] deve ser '1' → custo = número de '0's em s[i:n] = (prefix_zeros[n] - prefix_zeros[i])
        for i in range(n + 1):
            cost = prefix_ones[i] + (prefix_zeros[n] - prefix_zeros[i])
            if cost < min_cost:
                min_cost = cost
        
        # Candidata 4: prefixo de '1's e sufixo de '0's.
        # Para partição em i:
        # - s[0:i] deve ser '1' → custo = número de '0's em s[0:i] = prefix_zeros[i]
        # - s[i:n] deve ser '0' → custo = número de '1's em s[i:n] = (prefix_ones[n] - prefix_ones[i])
        for i in range(n + 1):
            cost = prefix_zeros[i] + (prefix_ones[n] - prefix_ones[i])
            if cost < min_cost:
                min_cost = cost
        
        print(min_cost)

if __name__ == "__main__":
    main()
