"""
#№8

import itertools


#m = list(itertools.permutations("ИГРА", 4))        #без повторений
m = list(itertools.product("ИГРА", repeat=4))       #c повторениями
m = ["".join(x) for x in m]
counter = 0
for s in m:
    if ("АГ" not in s) and ("АР" not in s) and ("ИГ" not in s) and ("ИР" not in s):
        print(s)
        counter += 1
print("Всего:", counter)

import itertools
#№8 10411

m = list(itertools.combinations_with_replacement("ABCX", 5))

print(m)

mass = ["".join(x) for x in m]
print(mass)

#№8  3193
a = {0: 'А', 1: 'О', 2: 'У'}
counter = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for h in range(0, len(a)):
                for l in range(0, len(a)):
                    counter += 1
                    if counter == 210:
                        print(a[i], a[j], a[g], a[h], a[l])


import itertools
m = list(itertools.product("АОУ", repeat=5))    #буквы могут повторяться
mass = ["".join(x) for x in m]                  #объеденяем строку
print(mass[210-1])              #выводим нужный элемент -1 тк начинаем с 0


#№8 3200
import itertools
m = list(itertools.product("АОУ", repeat=5))    #буквы могут повторяться
mass = ["".join(x) for x in m]                  #объеденяем строку
for i in range(len(mass)):
    if str(mass[i])[0] == "У":
        print(i + 1, mass[i])       #добавляем 1 т.к. начинается с 0
        break

#№8 3228
import itertools
m = list(itertools.product("АОУ", repeat=5))    #буквы могут повторяться
mass = ["".join(x) for x in m]                  #объеденяем строку
for i in range(len(mass)):
    if str(mass[i]) == "УАУАУ":
        print(i + 1, mass[i])       #добавляем 1 т.к. начинается с 0
        break


#3230
import itertools
m = list(itertools.product("АКРУ", repeat=5))
mass = ["".join(x) for x in m]
for i in range(len(mass)):
    if str(mass[i]) == "УКАРА":
        print(i+1)

#3232
import itertools
m = list(itertools.product("АКРУ", repeat=5))
mass = ["".join(x) for x in m]
for i in range(len(mass)):
    if mass[i] == "РУКАА":
        print(i+1)

#3515
import itertools
m = list(itertools.product("АОУ", repeat=5))
mass = ["".join(x) for x in m]
print(mass[101+1])

#14696
import itertools
m = list(itertools.product("АПРСУ", repeat=3))
mass = ["".join(x) for x in m]
print(mass)
for i in range(len(mass)):
    if str(mass[i])[0] == "С":
        print(i+1, mass[i])
        break

#35466
import itertools
m = list(itertools.product("АВЕИКНОР", repeat=3))     #абвгдеёжзийклмнопрстуфхцчшщьыъэюя
mass1 = ["".join(x) for x in m]
print(mass1)
mass2 = []
for i in range(len(mass1)):
    countB = 0
    if str(mass1[i])[0] == "B":
        countB += 1
    if str(mass1[i])[1] == "B":
        countB += 1
    if str(mass1[i])[2] == "B":
        countB += 1
    if countB == 1:
        mass2.append(mass1[i])
print(mass2)


#KEGE 190
import itertools

counter = 0
m = list(itertools.product("ABCDX", repeat=4))
mass = ["".join(x) for x in m]
for i in range(len(mass)):
    if mass[i].count("X") == 1:
        counter += 1
print(counter)

allCounter = 0
for i in range(100000, 1000000):
    countNesh = 0
    countFore = 0
    n = i
    string = str(i)
    countFore = int(string.count("4"))
    for j in range(6):
        if n % 10 == 1 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
            countNesh += 1
            n //= 10
        else:
            n //= 10
    if countFore == 1 and countNesh == 2:
        allCounter += 1
print(allCounter)

#KEGE 4613
import itertools
m = ["".join(x) for x in itertools.product("012345678", repeat=5)]
print(m, len(m), 9**5)

#KEGE КИМ № 25014273
import itertools
m = ["".join(x) for x in itertools.product("АНАСТАСИЯ", repeat=9)]
print(m)
glas = ["А", "И", "Я"]
sogl = ["Н", "С", "Т"]
counter = 0
for i in m:
    sttr = str(i)
    flag = False
    for j in range(9):
        if (sttr[j:j+1] in glas) and (sttr[j+1:j+2] in glas) and (sttr[j+2:j+3] in glas):
            if (sttr[j:j+1] in sogl) and (sttr[j+1:j+2] in sogl) and (sttr[j+2:j+3] in sogl):
                flag = True
    if flag == False:
        counter += 1
print(counter)

count = 0
for i in range(1,7):
    for x in range(0,7):
        for j in range(0, 7):
            for z in range(0, 7):
                for w in range(0, 7):
                    k = str(i)+str(x)+str(j)+str(z)+str(w)
                    if (i % 2 == 0) and (w >= 3) and (k.count("4") <= 1):
                        count += 1
print(count)

t1 = 90s
t2 = 40s
t упаковки = 13s
I = 50 Mb
40-13 = 27s
27/90=50/I2

#1979
import itertools
m = ["".join(x) for x in itertools.product("КРЕСЛО", repeat=4)]
glas = ["Е", "О"]
sogl = ["К", "Р", "С", "Л"]
counter = 0
for x in m:
    if (x[0] in sogl) and (x[-1] in glas):
        counter += 1
print(counter)

#1981
import itertools
m = ["".join(x) for x in itertools.product("ПУЛЯ", repeat = 6)]
counter = 0
for x in m:
    if x.count("У") == 2:
        counter += 1
print(counter)

#1982
import itertools
m = ["".join(x) for x in itertools.product("ЛОДКА", repeat = 4)]

c = 0

for x in m:
    if x.count("О") >= 2:
        c+=1
print(c)

#1983 САЛО
import itertools
m = ["".join(x) for x in itertools.product("САЛО", repeat=6)]
c=0
for x in m:
    if (x.count("О") >= 1) and (x.count("О") <= 3):
        c += 1
print(c)

#1984
import itertools
m = ["".join(x) for x in itertools.permutations("ИГРОК")]
c = 0
for x in m:
    if (x[0] != "К") and not("РОК" in x):
        c += 1
print(c)

#1415
import itertools
m = ["".join(x) for x in itertools.product("AB123", repeat = 8)]
c = 0
for x in m:
    if x.count("A") + x.count("B") == 2:
        c += 1
print(c)

#1216 -
def To5(a):
    base = 5
    dop = 0
    while a > 0:
        dop = a % base
        dop *= 10
        a //= base
    print(str(dop))
    return str(dop)
c = 0
for i in range(100,10000000):
    result = To5(i)
    #print(len(result), result[-1], result[0], result)
    if len(result) == 6:
        if (result[-1] != "3") and (result[-1] != "4") and (result[0] != "1"):
            c+=1
print(c)

#1288
import itertools
m = ["".join(x) for x in itertools.product("ВИШНЯ", repeat = 6)]
c = 0
for x in m:
    if x.count("В") <= 1:
        if x[0] != "Ш":
            if (x[-1] != "И") and (x[-1] != "Я"):
                c+=1
print(c)

#947 Ахуеть это что?
import itertools
m = ["".join(x) for x in itertools.product("1234", repeat = 4)]
print(m)
c = 0
for x in m:
    if x[0] <= x[1] <= x[2] <= x[3]:
        c += 1
print(c)

#1852
import itertools
m = ["".join(x) for x in itertools.product("ГЕПАРД", repeat=5)]
c=0
for x in m:
    if (x.count("Г") == 1) and (x[0] != "А") and (x[-1] != "Е"):
        c += 1
print(c)

#1921
c = 0
for i in range(100, 1000):
    x = str(i)
    if x[0] <= x[1] <= x[2]:
        c+= 1
print(c)

#1929
import itertools
mass = ["Д","Е","Й","К","С","Т","Р","А"]
m = ["".join(x) for x in itertools.product("ДЕЙКСТРА", repeat = 6)]
c = 0
sogl = ["Д","Й","К","С","Т","Р"]
for x in m:
    if x.count("Й") == 1:
        if x.index("Й") != len(x)-1:
            if (x[x.index("Й")+1] in sogl):
                f = 1
                for i in range(8):
                    if x.count(mass[i]) <= 1:
                        f = 1
                    else:
                        f=0
                        break
                if f == 1:
                    c+=1
print(c)

#5114 --
#6**3*2 + 2**2*6**2 + 2**3*30 + 10*6**2 = 1176 ++++
import itertools
s = ["".join(x) for x in itertools.product("123456", "0123456", "0123456", "0123456", "0123456")]
c = 0
for x in s:
    if s.count("5") == 1:
        if (("15" in s) or ("35" in s)) and (("51" in s) or ("53" in s)):
            c+= 1
print(c, 6**3*2 + 2**2*6**2 + 2**3*30 + 10*6**2)

#4613
import itertools
s = ["".join(x) for x in itertools.product("2468", "012345678", "012345678", "012345678", "0234567")]
c = 0
for x in s:
    if x.count("3") <= 1:
        c+= 1
print(c)

#1935
import itertools
m = ["".join(x) for x in itertools.permutations("ВАЙФУ", r=4)]
c=0
for x in m:
    if (x[0] != "Й") and not("ВФ" in x) and not("ФВ" in x):
        c+=1
print(c)

#1931
import itertools
print(len(set(itertools.permutations("МИМИКРИЯ"))))
#1961
print(int("1000",5) + 1)
#265
print(int("7724", 8) + 1)
#988
print(int("0314", 5)+1)

#989
import itertools
m = ["".join(x) for x in itertools.product("АИМРЯ", repeat=4)]
for i in range(len(m)):
    if i == 210:
        print(m[i])
"""
# 4668
# import itertools
# m = ["".join(x) for x in itertools.product("246", "0123456", "0123456", "0123456", "3456") if x.count("4") <= 1]
# print(len(m))

# import itertools
# m = ["".join(x) for x in itertools.product("0123456789", repeat = 9) if (x[0] != "0") and (len(set(x)) >= 3)]
# print(m[:10], len(m))

# 5663 -
# import itertools
# glas = ["A", "E", "I", "O", "U"]
# m = ["".join(x) for x in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=10) if (x.count("A")
#      + x.count("E") + x.count("I") + x.count("O") + x.count("U")) >= 2]
# print(len(m))
# print(m)

# 5663
# from math import factorial
# print(factorial(26)/factorial(16) - factorial(21)/factorial(11) - 50*factorial(21)/factorial(12))

# 5626
# import itertools
# m = ["".join(x) for x in itertools.product("246", "0123456", "0123456", "0123456", "01345") if x.count("7") <= 2]
# print(len(m))

# 5283 -
# import itertools
# m = [x for x in itertools.product("ABCDE", "ABC", "ABCDE", "AE")
#      if (x[0] != x[1]) and
#      ((x[0] in "AE" != x[2] in "AE") or ((x[0] in "BCD") != (x[2] in "BCD")))]
# print(len(m))

# пробник 30.01 -
# import itertools
# m = [''.join(x) for x in itertools.product("РУСЛАН", repeat=5) if x.count("У")+x.count("А") <= 1]
# print(len(m))

# import itertools
# m = [''.join(x) for x in itertools.permutations("1234567") if ("72" in x) or ("27" in x) or ("24" in x)]
# print(len(m))

# import itertools
# m = [''.join(x) for x in itertools.product("543424444444")]
# print(len(m))

# 6591
# import itertools
# print(len(["".join(x) for x in itertools.product("0123456", repeat=5) if (x[0] != '0') and (x.count("6") == 1) and (sum(int(y) for y in x if int(y) % 2 == 0) < sum(int(y) for y in x if int(y) % 2 != 0))]))

# import itertools
# m = [''.join(x) for x in itertools.permutations("12112121", r = 6) if (x.count("1") > x.count("2")) and (not("22" in x))]
# print(len(m), m[:100])

# 7610
# print(int("13000", 6))
# import itertools
# m = ["".join(x) for x in itertools.product("012345", repeat=5)]
# for i in range(len(m)):
#     if str(m[i])[:2] == "13":
#         print(i)

# import itertools
# m = ["".join(x) for x in itertools.product("АКРУ", repeat=5)]
# print(m[450+1])

# 7587
# print(int("2000", 5), int("0004", 5), int("0001", 5))
# import itertools
# m = [''.join(x) for x in itertools.product("АВЛОР", repeat = 4)]
# for i in range(len(m)):
#     if str(m[i])[0] == "Л":
#         print(i, m[i], i+1)
#         break
# 7810
# import itertools
# print(len(["".join(x) for x in itertools.product("МАСЛО", repeat=6) if (x.count("А") + x.count("О")) == 1]))

# import itertools
# m = ["".join(x) for x in itertools.permutations("ВИКОРТ", r=6)]
# print(m[170+1])

# print(int("3210", 4))
# import itertools
# m = [''.join(x) for x in itertools.product("БАЗИ", repeat=4)]
# for i in range(len(m)):
#     if m[i] == "ИЗБА":
#         print(i+1)

# 8364
# import itertools
# m = ["".join(x) for x in itertools.product("КРАТЕР", repeat=6)]
# c1 = c2 = 0
# for i in range(len(m)):
#     if m[i] == "КАРЕТА":
#         c1 = i
#     if m[i] == "РАКЕТА":
#         c2 = i
# print(c2-c1+1)

# 8496
# import itertools
# m = ["".join(x) for x in itertools.product("АВОРТ", repeat=6)]
# for i in range(len(m)):
#     if m[i] == "ВОРОТА":
#         print(i+1)

# 8945
# import itertools
# m1 = ["".join(x) for x in itertools.product("369", "124578AB", "0369", "124578AB", "0369", "124578AB", "0369")]
# m2 = ["".join(x) for x in itertools.product("124578AB", "0369", "124578AB", "0369", "124578AB", "0369", "124578AB")]
# print(len(m1) + len(m2))

# import itertools
# m = ["".join(x) for x in itertools.product("АКЛМНЯ", repeat=5)]
# c = 0
# for x in m:
#     if x[:2] == "МН":
#         c += 1
# print(c-2)

# import itertools
# m = [''.join(x) for x in itertools.product("АБИНРСТУ", repeat=5)]
# glas = ['А', "И", "У"]
# sogl = ["Б", "Н", "Р", "С", "Т"]
# for i in range(len(m)):
#     s = m[i]
#     if (s[0] == 'Н'):
#         if s[1] in glas and s[2] in sogl and s[3] in glas and s[4] in sogl:
#             print(i+1, m[i])

# import itertools
# m = ["".join(x) for x in itertools.product("АЕКНС", repeat=6)]
# for i in range(len(m)):
#     if m[i] == "СЕНЕКА":
#         print(i+1)

# import itertools
# m = ["".join(x) for x in itertools.product("АЕЛМНОРЬ", repeat=6)]
# firtM = -1
# for i in range(len(m)):
#     if m[i][:4] == "НОРМ" and firtM == -1:
#         firtM = i
#     if m[i] == "НЕНОРМ":
#         print(i-firtM-1)

# 9363
# import itertools
# m = [''.join(x) for x in itertools.permutations("ХОЧУНАБЮДЖЕТ")]
# print(m[:100])
# c = 0
# glas = "ОУАЮЕ"
# for i in range(len(m)):
#     dop = m[i]
#     for gl in glas:
#         dop = dop.replace(gl, "О")
#     if "ООООО" not in dop:
#         c += 1
# print(c, len(m))


# import itertools
# m = [''.join(x) for x in itertools.product("АКМСУ", repeat=5)]
# for i in range(len(m)):
#     if m[i] == "КУМАС":
#         print(i+1)

# import itertools
# m = ["".join(x) for x in itertools.product("ЭКЗАМЕН", repeat=8)
#      if abs((x.count("Э") + x.count("А") + x.count("Е")) -
#              (x.count("К") + x.count("З") + x.count("М") + x.count("Н"))) == 2 and x[3] != x[4]]
# print(len(m), m[:100])











