stroka = input()
word = ''
ind_1 = -1
ind_2 = -1
flag = 0
for i in range(len(stroka)):
    if stroka[i].isupper() and ind_1 == -1:
        word += stroka[i]
        ind_1 = i
    if stroka[i].isdigit() and ind_2 == -1:
        word += stroka[i + 1]
        ind_2 = i + 1
        ind_pred = ind_2
    if ind_1 > -1 and ind_2 > -1 and flag == 0:
        step = ind_2-ind_1
        if i - ind_pred == step:
            word += stroka[i]
            ind_pred = i
            if stroka[i] == '.':
                print(word)
                flag = 1