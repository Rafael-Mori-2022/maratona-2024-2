def main():
    n = int(input())
    mat = []

    for _ in range(n):
        mat.append(list(map(int, input().split())))

    s = mat[0][0]
    idx_i = 0
    idx_j = 0

    for i in range(n):
        for j in range(n):
            if mat[i][j] < s:
                s = mat[i][j]
                idx_i = i
                idx_j = j
    
    if idx_i == 0 and idx_j == 0:
        print(0)
    elif (idx_i == 0 and idx_j == (n-1)):
        print(1)
    elif (idx_i == (n-1) and idx_j == 0):
        print(3)
    else: 
        print(2)
     

if __name__ == "__main__":
    main()