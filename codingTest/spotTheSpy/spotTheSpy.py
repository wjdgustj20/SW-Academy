def diff_num(arr):
    std_num = 0
    for i, a in enumerate(arr):
        if i == 0:
            std_num = a
            continue
        elif i == 1:
            if a != std_num:
                if arr[2] == std_num:
                    return 2
                else:
                    return 1
        if a != std_num:
            return i + 1

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(diff_num(arr))
