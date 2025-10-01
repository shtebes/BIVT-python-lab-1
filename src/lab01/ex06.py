n = int(input())
online = 0
offline = 0
for i in range (n):
    stroka = input().split()
    if stroka[-1] == 'True': online+=1
    else: offline+=1
print(online,offline)
