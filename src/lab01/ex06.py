kol_player = int(input())
online = 0
offline = 0
for player in range(kol_player):
    stroka = input().split()
    if stroka[-1] == "True":
        online += 1
    else:
        offline += 1
print(online, offline)
