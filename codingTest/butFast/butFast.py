def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def isCorrect(a, b):
    if gcd(a, b) == 1:
        return "Perfect"
    else:
        return "Not even close"

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(isCorrect(a, b))
