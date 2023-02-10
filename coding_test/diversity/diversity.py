def maximum_score(n, s):
    diversity = []
    for i in range(n):
        left, right = [], []
        cnt_l, cnt_r = 0, 0
        for k in s[:i+1]:
            if k not in left:
                cnt_l += 1
                left.append(k)
        for k in s[i+1:]:
            if k not in right:
                cnt_r += 1
                right.append(k)
        diversity.append(cnt_l + cnt_r)
    return max(diversity)
            

n = int(input())
s = input()
print(maximum_score(n, s))
