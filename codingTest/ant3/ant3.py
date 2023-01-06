def isPossible(s, m):
    jun_idx = s.find('@')
    exit_idx = s.find('O')
    gauntlet_idx = s.find('G')

    if jun_idx > exit_idx:
        route = s[exit_idx:jun_idx+1]
    else:
        route = s[jun_idx:exit_idx+1]

    if route.count('#') <= m:
        return "HAHA!"

    if gauntlet_idx > jun_idx:
        route = s[jun_idx:gauntlet_idx+1]
    else:
        route = s[gauntlet_idx:jun_idx+1]

    if route.count('#') <= m:
        return "HAHA!"

    return "HELP!"

T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    s = input()
    print(isPossible(s, m))
