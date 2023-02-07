import heapq

def my_sum(arr, list):
    while True:
        if len(arr) == 1:
            return sum(list)
        target = heapq.heappop(arr) + heapq.heappop(arr)
        list.append(target)
        heapq.heappush(arr, target)

arr = list(map(int, input().split()))
heapq.heapify(arr)
print(my_sum(arr, []))
