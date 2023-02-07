def observe(builings, n):
    left_cnt = 0
    right_cnt = 0
    pre_height = 0

    for i in range(n):
        if i == 0:
            left_cnt += 1
            pre_height = builings[i]
        else:
            if builings[i] > pre_height:
                left_cnt += 1
                pre_height = buildings[i]

    for i in range(n-1,-1,-1):
        if i == n-1:
            right_cnt += 1
            pre_height = builings[i]
        else:
            if builings[i] > pre_height:
                right_cnt += 1
                pre_height = buildings[i]

    return left_cnt, right_cnt

n = int(input())
buildings = list(map(int, input().split()))
left_side, right_side = observe(buildings, n)
print(left_side, right_side)
