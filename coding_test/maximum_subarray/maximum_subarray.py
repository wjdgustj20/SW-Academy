def prefix_sum_array(n, arr):
    sum_array = []
    sum_array.append(arr[0])
    for i in range(1,n):
        sum_array.append(sum_array[i-1] + arr[i])
    return sum_array[-1]

def maximum_subarray(n, arr):
    result_set = []
    for l in range(n):
        for r in range(l, n):
            if l == 0:
                temp = prefix_sum_array(r+1, arr[:r+1])
            else:
                temp = prefix_sum_array(r+1, arr[:r+1]) - prefix_sum_array(l, arr[:l])
            result_set.append(temp)
    return max(result_set)
            

n = int(input())
arr = list(map(int, input().split()))
print(maximum_subarray(n, arr))
