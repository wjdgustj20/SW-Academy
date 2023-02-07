def sum(arr, start, end):
    sum = 0
    for i in range(start, end+1):
        sum = sum + arr[i]
    return sum

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for i in range(q):
    a, b = map(int, input().split())
    print(sum(arr, a-1, b-1))
