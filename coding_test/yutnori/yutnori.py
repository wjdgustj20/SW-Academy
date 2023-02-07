def yutnori(s):
    yut_rule = {1:1, 2:2, 3:3, 4:4, 0:5}
    cnt = 0
    for c in s:
        if c == '1':
            cnt += 1
    return yut_rule[cnt]

print(yutnori(input()))
