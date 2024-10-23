import math as mt

# Utilizar os menores valores primeiro a fim de preservar os valores maiores para construcao do resultado final
def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        a_list = list(map(int, input().split()))
        a_list.sort()

        while len(a_list) > 1:         
            new_value = mt.floor((a_list[0] + a_list[1])/2)

            a_list.pop(0)
            a_list.pop(0)

            a_list.insert(0, new_value)
            a_list.sort() # Precisamos manter a lista ordenada hehe =)

        print(a_list[0])
        

if __name__ == "__main__":
    main()