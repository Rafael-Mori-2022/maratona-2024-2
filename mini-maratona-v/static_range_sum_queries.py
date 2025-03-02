def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Build prefix sum array; prefix[0] is 0 for convenience.
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # Process each query and output the result.
    for _ in range(q):
        a, b = map(int, input().split())
        # Since the array is 1-indexed in the query, adjust accordingly.
        result = prefix[b] - prefix[a - 1]
        print(result)

if __name__ == "__main__":
    main()
