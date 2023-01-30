def isPangram(s):
    dict = { 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'f':0, 'k':0, 'l':0, 'm':0, 'n':0, \
             'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }
    if len(s) < 26:
        return "NO"
    else:
        s = s.lower().replace(" ", "")
        for c in s:
            dict[c] += 1
    for k, v in dict.items():
        if v == 0:
            return "NO"
    return "YES"

print(isPangram(input()))
