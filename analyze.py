from konlpy.tag import Kkma
from reader import *

polar, intens, express = filereader()
arrdict = []

for line in polar:
    arrdict.append(line)

komo = Kkma()

#file = open("data/input.txt", "r")
#lines = file.readlines()
#line = komo.pos(lines[0])
line = komo.pos(input("문장을 입력해주세요 : "))
line2 = []
for morph in line:
    line2.append([morph[0], morph[1]])
check = False
cnt, pos, neg, neut = 0, 0, 0, 0
temp_pos,temp_neg, temp_neut, temp_len = 0, 0, 0, 0
temp = []

line2.append([',', ','])

for index in range(len(line)):
    if cnt > 0:
        cnt -= 1
        continue
    for morph_polar in arrdict:
        arr = morph_polar['ngram'].split(';')
        arr2 = []
        for morph in arr:
            arr2.append((morph.split('/')))
        arr2.append([' ', ' '])
        check = True
        for i in range(len(arr2) - 1):
            if line2[index + i] == arr2[i]:
                cnt = i
                continue
            else:
                check = False
                break
        if check == True:
            temp_pos = morph_polar['POS']
            temp_neg = morph_polar['NEG']
            temp_neut = morph_polar['NEUT']
        else:
            pos += float(temp_pos)
            neg += float(temp_neg)
            neut += float(temp_neut)
            temp_pos, temp_neg, temp_neut = 0, 0, 0

if pos > neg:
    print("긍정적")
elif pos < neg:
    print("부정적")
else:
    print("중립적")
print('POS :', pos, 'NEG :', neg, 'NEUT :', neut)