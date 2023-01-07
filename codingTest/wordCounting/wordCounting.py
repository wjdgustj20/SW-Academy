def greatest(s):
    dict = {}
    size = len(s)
    for str in s:
        if str in dict:
            dict[str] += 1
        else:
            dict[str] = 1

    max_key = max(dict, key=dict.get)

    print(max_key, round(dict.get(max_key) / size, 2))

    
s = []
while True:
    try:
        ss = input().split()
        for str in ss:
            if str.isalpha():
                s.append(str.lower())
            else:
                s.append(str)
    except EOFError:
        break

greatest(s)
