def main():
    n = int(input())
    # Lê a linha com os n-1 inteiros: p2, p3, ..., pn
    parents = list(map(int, input().split()))
    
    # Cria um array "parent" indexado de 1 a n.
    # Para o 1º roteador, não há pai, então usamos -1.
    parent = [-1] * (n + 1)
    parent[1] = -1
    # Para os roteadores 2 a n, o pai do roteador i é parents[i-2]
    for i in range(2, n + 1):
        parent[i] = parents[i - 2]
    
    # Reconstrói o caminho do roteador n até o roteador 1
    path = []
    current = n
    while current != -1:
        path.append(current)
        current = parent[current]
    
    # Como o caminho foi construído de trás para frente, invertemos a lista
    path.reverse()
    
    # Imprime o caminho, separando os índices por espaço
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
