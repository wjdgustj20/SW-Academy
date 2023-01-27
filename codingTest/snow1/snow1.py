def ssuekssak(n, r1, c1, r2, c2):
    map = [['*' for _ in range(n)] for _ in range(n)]
    r1 -= 1
    r2 -= 1
    c1 -= 1
    c2 -= 1
    c_left, c_right, r_top, r_bottom = 0, 0, 0, 0
    if c1 < c2:
        c_left = c1
        c_right = c2
    else:
        c_left = c2
        c_right = c1

    if r1 < r2:
        r_top = r1
        r_bottom = r2
    else:
        r_top = r2
        r_bottom = r1

    for i in range(r_top, r_bottom+1):
        for j in range(c_left, c_right+1):
            map[i][j] = '.'

    return map

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

for r in ssuekssak(n, r1, c1, r2, c2):
    for c in r:
        print(c, end="")
    print()
