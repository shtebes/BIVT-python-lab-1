stroka = input()
word =''
ind1 = -1
ind2 = -1
k = 0
for i in range(len(stroka)):
    if stroka[i].isupper() and ind1 == -1:
        word += stroka[i]
        ind1 = i
    if stroka[i].isdigit() and ind2 == -1:
        word += stroka[i + 1]
        ind2 = i + 1
        indp = ind2
    if ind1 > -1 and ind2 > -1 and k == 0:
        step = ind2-ind1
        if i - indp == step:
            word+=stroka[i]
            indp = i
            if stroka[i] == '.':
                print(word)
                k = 1