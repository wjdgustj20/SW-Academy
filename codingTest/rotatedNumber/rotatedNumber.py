def find(n):
    answer = 0
    if n % 2 == 0:
        k = int(n / 2)
        answer = 5 ** k - 5 ** (k - 1)
    else:
        k = int(n // 2)
        answer = 5 ** k * 3 - 5 ** (k - 1) * 3

    return answer

n = int(input())
print(find(n))
