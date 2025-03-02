def main():
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # Calcula a soma do primeiro bloco de k planks
    current_sum = sum(heights[:k])
    min_sum = current_sum
    min_index = 0  # índice (0-indexado) do bloco com menor soma
    
    # Usa janela deslizante para avaliar os blocos subsequentes
    for i in range(1, n - k + 1):
        current_sum = current_sum - heights[i - 1] + heights[i + k - 1]
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i
            
    # Imprime o índice (1-indexado) do primeiro plank do bloco ideal
    print(min_index + 1)

if __name__ == "__main__":
    main()
