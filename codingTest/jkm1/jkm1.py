def sell(n, a, m, k):
    buy = a[k-1]
    for i in range(k, len(a)):
        if a[i] >= buy + m:
            return i + 1
    return "JB"

T = int(input())
for i in range(T):
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(sell(n, a, m, k))
