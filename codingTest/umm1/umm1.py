def isUmm(s, a, b):
    str = s[a-1:b]
    if str[0] != 'U':
        return "NO"
    if len(str) < 3:
        return "NO"
    for i in range(1, len(str)):
        if str[i] != 'm':
            return "NO"
    return "YES"

T = int(input())
for i in range(T):
    n = int(input())
    s = input()
    a, b = list(map(int, input().split()))
    print(isUmm(s, a, b))
