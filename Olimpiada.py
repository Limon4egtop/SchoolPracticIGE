"""#КИМ № 25016609
#2
print("w y z x")
for w in 0,1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = w <= ((x<=z) <= y)
                if f == 0:
                    print(w, y, z, x)

#5
print(bin(15)[2:])
for i in range(1,16):
    n = bin(i)[2::]
    if n.count("1") % 2 == 0:
        n = "10" + n[2:] + "1"
    else:
        n = "11" + n[2:] + "0"
    print(i,bin(i)[2:], n, int(n, 2))  #11

#7
print(14.285 * 2**23/2/44000/135)

#8
import itertools
m = ["".join(x) for x in itertools.product("АРБУЗ", repeat = 6)]
c = 0
for x in m:
    if ("АА" in x) and not("ААА" in x) and (x.count("А") == 3):
        c += 1
print(c)

#11
print(4560, 2**12, 2**13, 294*13/8, 478*131072/1024)

#12
c = 0
for n in range(1, 100+1):
    s = "1" + "0" * n
    while ("10" in s) or ("1" in s):
        if "10" in s:
            s = s.replace("10", "0001", 1)
        else:
            if "1" in s:
                s = s.replace("1", "0", 1)
    if len(s) % 7 == 0:
        c+=1
print(c)

#14
for n in range(1,1000):
    z = 1*n**2 + 1*n**1 + 0*n**0
    if z == 39800:
        print(n)
"""
#15
"""
c = 0
for x in range(1, 1000):
    for a in range(1, 1000):
        for b in range(160, 180+1):
            f = (160 <= x <= 180) <= ((x%35 == 0) <= (x%a == 0))
            if f == 1:
                c+=1
print(c)

def f(x):
    return (160<=x<=180) <= ((x%35 == 0) <= (x%a == 0))

for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 10000)):
        print(a)

#16
from sys import *
def f(n):
    if n >= 10000:
        return n
    if n %2 == 0:
        return f(n+2) - 3
    if n % 2 != 0:
        return f(n+2) + 1

setrecursionlimit(10000)
print(f(94) - f(80))

#17
with open("*.txt") as f:
    m = [int(x) for x in f]

ans = []
xMin = 100000000000
xMax = -10000000000

for x in m:
    if (x != 8) and (x%8 == 0) and (x < xMin):
        xMin = x


for i in range(len(m) - 1):
    if (m[i] % xMin == 0) and (m[i+1] % xMin == 0):
        ans.append(m[i] + m[i+1])
print(len(ans), min(ans))
for i in range(len(m) - 1):
    if m[i]+m[i+1] == min(ans):
        print(m[i], m[i+1])
"""

#Статград 18.12.22
#2
# print("x y w z  f")
# for w in 0,1:
#     for z in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (x == (not(y))) <= ((z <= (not(w))) and (w <= y))
#                 if x+y+w+z == 3 and f == 1:
#                     print( x, y, w, z, "", int(f))
#                 if f == 0:
#                     print(x, y, w, z, "", int(f))

#5
# for i in range(1,290):
#     st1 = i
#     n1 = bin(st1)[2:]
#     summ1 = 0
#     while st1 > 0:
#         summ1 += st1 % 10
#         st1 //= 10
#     if summ1 % 2 == 0:
#         n1 += "0"
#     else:
#         n1 += "1"
#     st1 = int(n1, 2)
#     n1 = bin(st1)[2:]
#     summ1 = 0
#     while st1 > 0:
#         summ1 += st1 % 10
#         st1 //= 10
#     if summ1 % 2 == 0:
#         n1 += "0"
#     else:
#         n1 += "1"
#     st1 = int(n1, 2)
#     n1 = bin(st1)[2:]
#     summ1 = 0
#     while st1 > 0:
#         summ1 += st1 % 10
#         st1 //= 10
#     if summ1 % 2 == 0:
#         n1 += "0"
#     else:
#         n1 += "1"
#
#     if int(n1,2) > 2054:
#         print(int(n1,2))

#7
# print(15*100*2**23/75, 167772160/200/200, 4194.304*300*300*60/100/2**23)

# 8
# import itertools
# m = ["".join(x) for x in itertools.product("ПОЛИНА", repeat=8)]
# c = 0
# for x in m:
#     if x.count("П") + x.count("Л") + x.count("Н") > x.count("О") + x.count("И") + x.count("А"):
#         c += 1
# print(c)

# 11
# print(310*10, 3100/8, 388*16384, 6356992/1024)

#12
# import itertools
# m = ["0"+"".join(x)+"0" for x in itertools.product("12", repeat=20) if x.count("1") == 10]
# for s in m:
#     while "00" not in s:
#         s = s.replace("012", "30", 1)
#         if "011" in s:
#             s = s.replace("011", "20", 1)
#             s = s.replace("022", "40", 1)
#         else:
#             s = s.replace("01", "10", 1)
#             s = s.replace("02", "101", 1)
#     if s.count("1") == 7 and s.count("2") == 5:
#         print(s.count("3"))
#         break

# 12
# import itertools
# m = ["0" + "".join(x) + "0" for x in itertools.product("12", repeat = 20) if x.count("1") == 10]
# maxx = -100000
# for s in m:
#     while "00" not in s:
#         s = s.replace("012", "30", 1)
#         if "011" in s:
#             s = s.replace("011", "20", 1)
#             s = s.replace("022", "40", 1)
#         else:
#             s = s.replace("01", "10", 1)
#             s = s.replace("02", "101", 1)
#     # print(s.count("1"), s.count("2"), s.count("4"))
#     if (s.count("1") == 6) and (s.count("2") == 5):
#         maxx = max(maxx, s.count("4"))
# print(maxx)

# 14
# for x in range(100):
#     z = (3*37**3 + 1*37**2 + 7*37**1 + x*37**0) + (4*37**3 + x*37**2 + 2*37**1 + 9*37**0)
#     if z % 36 == 0:
#         print(z / 36, x)

# 15
# for A in range(1, 500):
#     f = 1
#     for x in range(1, 100):
#         for y in range(1, 100):
#             z = ((108 % x == 0) <= (x % y != 0)) or (x + y > 80) or (A - y > x)
#             if z == 1:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(A)
#         break

# 16 -
# from sys import *
# setrecursionlimit(100000)
# def f(n):
#     if n == 0:
#         return 0
#     if n > 0:
#         return f(n // 10) + (n % 10)
# c = 0
# for i in range(237567892, 1134567009+1):
#     if f(i) > f(i+1):
#         c+=1
# print(c)

# 16
# c = 0
# for i in range(237567892, 1134567009+1):
#     if i % 10 == 9:
#         c+= 1
# print(c)        #89699912

# 17
# with open("*.txt") as f:
#     m = [int(x) for x in f]
# xMin = 100000000
# xMax = -100000000
# c = 0
#
# for x in m:
#     xMin = min(x, xMin)
#
# for i in range(len(m) - 1):
#     if m[i] > m[i+1]:
#         if str(m[i+1])[-1] == "3":
#             kv1 = m[i] * m[i]
#             kv2 = m[i + 1] * m[i + 1]
#             if ((kv1 + kv2) < xMin * xMin) and (str(m[i])[-1] == "3") and (str(m[i+1])[-1] == "3"):
#                 c+=1
#                 xMax = max(xMax, m[i]*m[i] + m[i+1]*m[i+1])
#     else:
#         if str(m[i])[-1] == "3":
#             kv1 = m[i] * m[i]
#             kv2 = m[i + 1] * m[i + 1]
#             if ((kv1 + kv2) < xMin * xMin) and (str(m[i])[-1] == "3") and (str(m[i+1])[-1] == "3"):
#                 c += 1
#                 xMax = max(xMax, m[i] * m[i] + m[i + 1] * m[i + 1])
# print(c, xMax)

#22
# s = open("*.txt").read()
# s = s.replace("F", " ").split()
# print(max(len(x) for x in s if x.count("A") <= 2))

# Информатика. 11 класс. Вариант ИН2210202
# 2
# print('w x y z  f')
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (z == (not(x))) <= ((w <= (not(y))) and (y <= x))
#                 if x+y+w+z == 3 and f == 1:
#                     print(w,x,y,z,"",f.real)
#                 if f == 0:
#                     print(w, x, y, z, "", f.real)
# 5
# for i in range(1, 300):
#     n = i
#     st = bin(n)[2:]
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     if summ % 2 == 0:
#         st += "0"
#     else:
#         st += "1"
#
#     n = int(st, 2)
#     st = bin(n)[2:]
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     if summ % 2 == 0:
#         st += "0"
#     else:
#         st += "1"
#
#     n = int(st, 2)
#     st = bin(n)[2:]
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     if summ % 2 == 0:
#         st += "0"
#     else:
#         st += "1"
#
#     if int(st,2) > 1028:
#         print(i, int(st,2))
# 7
# print(4*2**23*100/80/150/150, 1864.135111111111*300*300*60/100/2**23)
# 8
# import itertools
# m = ["".join(x) for x in itertools.product("ВЕРОНИКА", repeat = 6)]
# c = 0
# for x in m:
#     if x.count("Е") + x.count("О") +  x.count("И") +  x.count("А") > x.count("В") + x.count("Р") + x.count("Н") + x.count("К"):
#         c += 1
# print(c)
# 11
# print(2**10, 290*10, 2900/8, 363*32768/1024)
# 15
# for A in range(1,10000):
#     f = 1
#     for x in range(1,1000):
#         for y in range(1, 1000):
#             z = ((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (A - x > y)
#             if z == 1:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(A)
# 17
# with open("*.txt") as f:
#     m = [int(x) for x in f]
# m = [71, 15, 25, 10, 8, 12, 15, 12, 55, -5, -10, -15, -25]
# xMax = -100000000
# xMin = 1000000000
# c = 0
# for x in m:
#     xMin = min(xMin, x)
# for i in range(len(m) - 1):
#     print(str(m[i]), str(m[i])[-1], str(m[i+1]), str(m[i+1])[-1])
#     if m[i] > m[i+1]:
#         if str(m[i+1])[-1] == "5":
#             if str(m[i+1])[-1] == "5" and str(m[i])[-1] == "5":
#                 c += 1
#                 xMax = max(m[i] + m[i+1], xMax)
#     else:
#         if str(m[i])[-1] == "5":
#             if str(m[i+1])[-1] == "5" and str(m[i])[-1] == "5":
#                 c += 1
#                 xMax = max(m[i] + m[i+1], xMax)
# print(c, xMax)












































































