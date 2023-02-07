def song(a, b, q):
    time = 1
    time_line = {}
    play_list = []
    for i in range(len(b)):
        time_line[a[i]] = (time, time+b[i]-1)
        time += b[i]

    for t in q:
        for k, v in time_line.items():
            s, e = v
            if s <= t <= e:
                play_list.append(k)

    return play_list


n = int(input())
a = []

for i in range(n):
    a.append(input())

b = []
for i in range(n):
    b.append(int(input()))

m = int(input())
q = []
for i in range(m):
    q.append(int(input()))

for s in song(a, b, q):
    print(s)
