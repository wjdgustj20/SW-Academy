t = int(input())

for i in range(t):
    n = int(input())
    bike = list(map(int, input().split()))
    m = int(input())

    for j in range(m):
        u, v = list(map(int, input().split()))
        bike[u-1] = bike[u-1] - 1
        bike[v-1] = bike[v-1] + 1

    for n in bike:
        print(n, end=' ')
    print()