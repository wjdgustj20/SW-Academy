def stalin(arr):
    # for i, a in enumerate(arr):
    #     if i >= len(arr) - 1:
    #         break
    #
    #     j = i+1
    #     while j < len(arr):
    #         if a > arr[j]:
    #             del arr[j]
    #             continue
    #         j += 1
    l = len(arr)
    std = arr[0]
    answer = []

    return arr

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for a in stalin(arr):
        print(a, end=' ')
    print()