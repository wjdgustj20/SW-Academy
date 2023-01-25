def solution(a, money):
    cnt_less = 0
    cnt_more = 0

    for m in money:
        if a == m:
            continue
        elif a < m:
            cnt_more += 1
        else:
            cnt_less += 1

    return cnt_less, cnt_more

n = int(input())
money = list(map(int, input().split()))
for a in money:
    l, m = solution(a, money)
    print(l, m)
