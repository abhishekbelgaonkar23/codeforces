username = input().strip()

dis = set(username)

if len(dis) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
