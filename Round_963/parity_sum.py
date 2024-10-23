# Link util para entendimento da solucao: https://www.youtube.com/watch?v=Qmyvy8-4SH4

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        a_list = list(map(int, input().split()))

        greastest_odd = -1
        even_list = []

        for a in a_list:
            if a % 2 == 0:
                even_list.append(a)
            elif a > greastest_odd:
                greastest_odd = a

        even_list.sort()

        if even_list == [] or len(even_list) == n: # Ha apenas uma paridade
            print(0)
            continue
        
        counter = len(even_list)
        for even in even_list:
            if even < greastest_odd:
                greastest_odd += even 
            else:
                counter += 1 # Sinal que e necessario o caso aj = ai + aj a mais, incrementa uma operacao no total
                break

        print(counter)
            

if __name__ == "__main__":
    main()