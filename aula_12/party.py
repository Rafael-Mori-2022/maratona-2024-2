def main():
    n = int(input().strip())
    # managers[i] guarda o gerente imediato do empregado i+1; se for -1, o empregado não tem gerente
    managers = [int(input().strip()) for _ in range(n)]
    
    max_depth = 0
    # Para cada empregado, calculamos a profundidade (ou seja, o comprimento da cadeia até a raiz)
    for i in range(n):
        depth = 0
        cur = i
        # Percorre a cadeia de gerência até encontrar um empregado sem gerente (-1)
        while cur != -1:
            depth += 1
            if managers[cur] == -1:
                break
            # Como os empregados são numerados de 1 a n, convertemos para 0-indexado:
            cur = managers[cur] - 1
        max_depth = max(max_depth, depth)
    
    print(max_depth)

if __name__ == "__main__":
    main()
