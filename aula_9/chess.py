def main():
    t = int(input().strip())
    
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        total = p1 + p2 + p3
        
        # Total de pontos deve ser par, pois cada jogo rende 2 pontos no total.
        if total % 2 != 0:
            print(-1)
            continue
        
        # Número total de jogos
        G = total // 2
        
        # Para cada jogador, se ele tivesse participado só de empates, seu placar seria igual
        # ao número de jogos em que participou. Assim, é necessário que:
        # ⎡pᵢ/2⎤ ≤ G  para i = 1, 2, 3.
        if (p1 + 1) // 2 > G or (p2 + 1) // 2 > G or (p3 + 1) // 2 > G:
            print(-1)
            continue
        
        # Para cada jogador, se ele participou de G jogos e fez pᵢ pontos, o “excesso”
        # que não pode ser explicado só por empates (1 ponto por jogo) deve vir de vitórias,
        # que rendem 2 pontos. Assim, o número mínimo de vitórias necessárias para o jogador i é:
        # wᵢ,min = max(pᵢ - G, 0)
        w1_min = max(p1 - G, 0)
        w2_min = max(p2 - G, 0)
        w3_min = max(p3 - G, 0)
        
        wins_min = w1_min + w2_min + w3_min
        
        # Como cada jogo é ou vitória/derrota ou empate, temos:
        # total de jogos = (jogos com vitória) + (jogos empatados).
        # Queremos maximizar os empates, isto é:
        # empates_max = G - (mínimo de jogos com vitória)
        ans = G - wins_min
        print(ans)

if __name__ == "__main__":
    main()
