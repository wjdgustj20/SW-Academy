def take_time(n, arr):
    minimum = min(arr)
    time = 0
    for a in arr:
        if a > minimum:
            time += a - minimum
    return time

n = int(input())
arr = list(map(int, input().split()))
print(take_time(n, arr))
