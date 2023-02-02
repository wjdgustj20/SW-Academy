def leastMirror(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return 0
    else:
        return 1

x1, y1, x2, y2 = list(map(int, input().split()))
print(leastMirror(x1, y1, x2, y2))
