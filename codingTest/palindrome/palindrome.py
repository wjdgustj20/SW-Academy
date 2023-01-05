def isPalindrome(str, n):
    if n < 0:
        return False
    length = len(str)
    for i in range(length):
        if str[i] != str[length-1-i]:
            return isPalindrome(str.replace(str[i], '', 1), n-1) or isPalindrome(str.replace(str[length-1-i], '', 1), n-1)
    return True

input = input().split()
str = input[0]
n = int(input[1])
print(isPalindrome(str, n))
