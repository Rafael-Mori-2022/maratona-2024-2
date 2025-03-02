def main():
    n = int(input())
    # Read the n-1 numbers and convert them to integers.
    numbers = list(map(int, input().split()))
    
    # Compute the expected sum of numbers from 1 to n.
    total = n * (n + 1) // 2
    
    # The missing number is the difference between the expected sum and the actual sum.
    missing = total - sum(numbers)
    print(missing)

if __name__ == "__main__":
    main()
