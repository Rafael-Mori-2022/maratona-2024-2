def main():
    n = int(input())
    k = int(input())

    if (n > 1):
        max_talk_time = (k - (n - 1)) // n  
        print(max_talk_time)
    else:
        print(k)


if __name__ == "__main__":
    main()