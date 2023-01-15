def my_round(n):
    temp = n * 1000 % 10
    if temp >= 5:
        return round(n + 0.005, 2)
    else:
        return round(n, 2)

T = int(input())
for i in range(T):
    n, u = list(input().split())
    if u == 'M':
        print(my_round(int(n) * 1.6))
    elif u == 'K':
        print(my_round(int(n) * (1 / 1.6)))
