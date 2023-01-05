def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for s in str1:
        if s in str2:
            str2 = str2.replace(s, '', 1)
        else:
            return False
    if len(str2) != 0:
        return False
    return True

s = input().split()
str1 = s[0]
str2 = s[1]
print(isAnagram(str1, str2))
