n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(m):
    l, r = map(int, input().split())
    print(sum(arr[l-1:r]))
