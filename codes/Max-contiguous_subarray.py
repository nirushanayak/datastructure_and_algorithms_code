def max_contigous_sum(num, arr):
    maxIndex = arr[0]
    maxSoFar = arr[0]
    for i in range(1, num):
        maxIndex = max(arr[i], maxIndex + arr[i])
        maxSoFar = max(maxIndex, maxSoFar)
    return maxSoFar



num = int(input())
arr = list(map(int, input().split()))
print(max_contigous_sum(num, arr))

