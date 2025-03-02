def main():
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        path = input().strip()
        
        # dp[i] armazenará o máximo de moedas coletadas ao alcançar a célula i.
        dp = [-10**9] * n  
        dp[0] = 0 
        
        for i in range(n):
            if dp[i] < 0:
                continue
            for move in (1, 2):
                j = i + move
                if j < n and path[j] != '*':  # Verifica se a célula j está no caminho e não possui espinhos.
                    # Se a célula j contém moeda, incrementa 1; caso contrário, permanece o mesmo.
                    coin = 1 if path[j] == '@' else 0
                    dp[j] = max(dp[j], dp[i] + coin)
                    
        print(max(dp))
        
if __name__ == "__main__":
    main()
