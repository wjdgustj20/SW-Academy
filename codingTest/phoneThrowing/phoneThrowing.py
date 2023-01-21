def find_min(k,n):
    cnt = 0
    while True:
        cnt += 1
        if n == 1:
            return cnt
        n = n // 2

k, n = list(map(int, input().split()))
print(find_min(k,n))
