def stalin(arr):
    change = True

    while (change):
        change = False
        for i, a in enumerate(arr):
            if i >= len(arr) - 1:
                break
            if a > arr[i+1]:
                arr[i] = arr[i] // 2
                change = True

    return arr

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for a in stalin(arr):
        print(a, end=' ')
    print()
