def adventure(n, m, s, go):
    x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    y = {'L': 0, 'R': 0, 'U': -1, 'D': 1}

    for r, a in enumerate(s):
        jun_x = a.find('@')
        if jun_x == -1:
            continue
        else:
            jun_y = r
            break

    damage = 0
    for d in go:
        next_y, next_x = jun_y + y[d], jun_x + x[d]

        if s[jun_y][jun_x] == '^':
            damage += 1

        if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m or s[next_y][next_x] == '#':
            continue
        else:
            jun_y, jun_x = next_y, next_x
            
    if s[jun_y][jun_x] == '^':
        damage += 1

    return jun_y + 1, jun_x + 1, damage


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    k = int(input())
    go = list(input())
    r, c, d = adventure(n, m, s, go)
    print(r, c, end=' ')
    print(d)
