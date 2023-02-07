def prefix_sum_array(n, arr):
    sum_array = []
    sum_array.append(arr[0])
    for i in range(1,n):
        sum_array.append(sum_array[i-1] + arr[i])
    return sum_array

n = int(input())
arr = list(map(int, input().split()))
for a in prefix_sum_array(n, arr):
    print(a, end=' ')
