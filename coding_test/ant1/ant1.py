def isPossible(s):
    if s.count('#') >= 2:
        return "HELP!"
    else:
        return "HAHA!"

s = input()
print(isPossible(s))
