def main():
    n = int(input().strip())
    cards = list(map(int, input().split()))
    
    sereja = 0  
    dima = 0    
    turn = 0    
    
    while cards:
        # Escolhe a carta com o maior valor entre a esquerda e a direita
        if cards[0] > cards[-1]:
            chosen = cards.pop(0)
        else:
            chosen = cards.pop(-1)
        
        # Acumula os pontos de acordo com o jogador que está jogando
        if turn == 0:
            sereja += chosen
        else:
            dima += chosen
        
        # Alterna a vez do jogador
        turn = 1 - turn
        
    print(sereja, dima)
    
if __name__ == "__main__":
    main()
