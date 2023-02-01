def bestsushi(n, arr):
    best_idx = 0
    for i in range(n):
        if abs(320-arr[i]) < abs(320-arr[best_idx]):
            best_idx = i
    return best_idx + 1
        

n = int(input())
arr = list(map(int, input().split()))
print(bestsushi(n, arr))
