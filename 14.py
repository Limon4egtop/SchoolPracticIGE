""""#KEGE 497
n = 5**94 + 25**49 - 130
base = 5
counter = 0
while n > 0:
    a = n % base
    if a == 4:
        counter += 1
    n //= base
print(counter)

#KEGE 431
base = 7
a = None
for x in range(100):
    summ = 0
    n = 3 * 7**(x+1) + 13*7**(x+2) + 31*7**(x*3) + 1*7**(x*2)
    while n > 0:
        a = n % base
        n //= base
        summ += a
    if summ == 18:
        print(x)

#KEGE 2934
n = 6 * 512**180 + 7 * 64**181 + 3 * 8**184 + 5*8**125 - 65
base = 64
counter = 0
while n > 0:
    a = n % base
    if a == 0:
        counter += 1
    n //= base
print(counter)

#KEGE 4937
for x in range(80):
    n1 = 3 * 80**3 + x * 80**2 + 7 * 80 + 5
    n2 = 80**3 + 4 * 80**2 + x * 80
    n = n1+n2
    if n % 17 == 0:
        print(x, n / 17)        #146405

for i in range(100):
    x = str(i)
    a = int("2"+x+"BAD",16) + int("3C"+x+"FE", 16)
    if a % 15 == 0:
        print(i)

#KEGE 4937
for x in range(1, 80):
    chislo = (3*80**3 + x*80**2 + 7*80**1 + 5*80**0) + (1*80**3 + 4*80**2 + x*80**1+0*80**0)
    if (chislo) % 17 == 0:
        print(x, chislo//17)

#4962
for x in range(1,1000):
    summ = int(f"3364{x}", 11) + int(f"{x}7946", 12)
    chislo = int(f"55{x}87", 14)
    if summ == chislo:
        print(x, summ, chislo)

#58
print(oct(64**30 + 2**300 - 4)[2:].count("7"))

#233
x = 3 * 16**8 - 4**5 + 3
c = 0
while x > 0:
    if x % 4 == 3:
        c += 1
    x //= 4
print(c)

#234
x = 2 * 27**7 + 3**10 - 9
c = 0
while x > 0:
    if x % 3 == 0:
        c+= 1
    x //=3
print(c)

#387
x = 51 * 7**12 - 7**3 - 22
summ = 0
while x >0:
    summ += x%7
    x//=7
print(summ)

#1071
for i in range(1, 10000):
    x = 125**200 - 5**i + 74
    c = 0
    while x > 0:
        if x % 5 == 4:
            c += 1
        x //= 5
    if c == 100:
        print(i)

#1120
for x in range(1,20000):
    if bin(4**2015 + 2**x - 2**2015 + 15)[2:].count("1") == 500:
        print(x)

#1121
for x in range(1,10000):
    if bin(4**1014 - 2 ** x + 12)[2:].count("0") == 2000:
        print(x)

#1122
for x in range(1,10000):
    a = 36**17 - 6**x + 71
    summ = 0
    while a > 0:
        summ += a % 6
        a //= 6
    if summ == 61:
        print(x)

#2033
z = 6 * 144**26 + 11 * 12**75 - 48
c = 0
while z > 0:
    if z % 12 == 11:
        c += 1
    z //= 12
print(c)

#1222
z = 5 * 216**1156 - 4 * 36**1147 + 6**1153 - 875
c5 = 0
c0 = 0
while z > 0:
    if z % 6 == 5:
        c5 += 1
    if z % 6 == 0:
        c0 += 1
    z//=6
print(c5-c0)

#241
for x in range(1000):
    z = (3*(x+4)**1 + 3*(x+4)**0) - (3*4**1 + 3*4**0)
    if z == 33:
        print(x)

#242
for n in range(1000):
    if (1*n**2 + 0*n**1 + 3*n**0) == (9*(n+2)**1 + 7*(n+2)**0):
        print(n)

#243
for n in range(1000):
    if (1*n**2 + 3*n**1 + 2*n**0) + (1*8**1 + 3*8**0) == (1*(n+1)**2 + 2*(n+1)**1 + 4*(n+1)**0):
        print(n)

#244
for x in range(1, 1000):
    if (2*x**1 + 1*x**0) * (1*x**1 + 3*x**0) == (3*x**2 + 1*x**1 + 3*x**0):
        print(x)

#249
for i in range(21, 30):
    x = i
    x3 = ""
    while x > 0:
        x3 += str(x%3)
        x //= 3
    print(x3[:2], i) #ответ 22

#250
print(bin(27))

#251
# for i in range(1,1000):
#     n = i
#     x = 6*n**1 + 8*n**0
#     if (len(str(x)) == 4) and (str(x)[-1] == "2"):
#         print(n)
for n in range(2,20):
    if 68%n == 2 and n**3<=68<=n**4:
        print(n)

#256
# def ToX(n, base):
#     s = ""
#     while n >0:
#         s += str(n % base)
#         n //= base
#     return s
#
# for i in range(1,100):
#     toSix = ToX(i, 6)
#     toFive = ToX(i, 5)
#     toEleven = ToX(i, 11)
#     if (len(toSix) == 2) and (len(toEleven) == 3) and (toEleven[-1] == "1"):
#         print(i)
for n in range(1,100):
    if (int('10', 6) <= n <= int("100", 6)) and (int('100', 5) <= n <= int("1000", 5)) and (n%11 == 1):
        print(n)

#257
for n in range(1, 100):
    if (int("10", 7) <= n <= int("100",7)) and (int("100", 6) <= n <= int("1000", 6)) and n%13 == 3:
        print(n)

#385
c = 0
for n in range(1,10000):
    if (n <= int("10000", 5)) and (n >= int("10000", 2)) and (n % 16 == 12):
        c+=1
print(c)

#4702
for x in range(15):
    z = (1*15**4 + 2*15**3 + 3*15**2 + x*15**1 + 5*15**0) + (1*15**4 + x*15**3 + 2*15**2 + 3*15**1 + 3*15**0)
    if (z % 14 == 0):
        print(x%14, z//14)  #8767

#4961
for x in range(17):
    z = (9*17**4 + 7*17**3 + 5*17**2 + 9*17**1 + x*17**0) + (3*17**4 + x*17**3 + 1*17**2 + 0*17**1 + 8*17**0)
    if z % 11 == 0:
        print(x%11  , z//11)

#4962
for x in range(100):
    z1 = (3*11**4 + 3*11**3 + 6*11**2 + 4*11**1 + x*11**0) + (x*12**4 + 7*12**3 + 9*12**2 +4*12**1 +6*12**0)
    z2 = 5*14**4 + 5*14**3 + x*14**2 + 8*14**1 + 7*14**0
    if z1 == z2:
        print(z2)

#4963
for x in range(15):
    for y in range(17):
        z = (1*15**4 + 2*15**3 + 3*15**2 + x*15**1 + 5*15**0) + (6*17**3 + 7*17**2 + y*17**1 + 9*17**0)
        if z%131 == 0:
            print(x, y, z//131)

#4964
for x in range(21):
    f = 1
    for y in range(21):
        z = (1*21**4 + 2*21**3 + y*21**2 + x*21**1 + 9*21**0) + (3*21**4 + 6*21**3 + y*21**2 + 9*21**1 + 9*21**0)
        if z % 18 == 0:
            f = 1
        else:
            f = 0
            break
    if f == 1:
        y = 5
        z = (1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 ** 1 + 9 * 21 ** 0) + (
                    3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 ** 1 + 9 * 21 ** 0)
        print(z//18)
"""

# 5669
# for x in range(16):
#     s = (8*16**4 + 5*16**3 + 6*16**2 + 9*16**1 + x*16**0) + (1*16**4 + 2*16**3 + x*16**2 + 4*16**1 + 8*16**0)
#     ss = oct(s)[2:]
#     if (ss.count("2") + ss.count("4") + ss.count("6")) <= 2:
#         print(ss)

# 5632
# for i in range(21):
#     f = 1
#     for j in range(1, 21, 2):
#         z = int("32" + str(i) + str(j) + "A", 21) + int("16" + str(j) + "18", 21)
#         if z % 12 == 0 and j % 2 != 0:
#             f = 0
#             break
#         else:
#             f = 1
#     if f == 1:
#         z = int("32" + str(i) + "7" + "A", 21) + int("16" + "7" + "18", 21)
#         print(z / 12)

# 5289
# c = 0
# for x in range(18):
#     z = (5*18**3 + 6*18**2 + x*18**1 + 3*18**0) + (4*18**2 + x*18**1 + 9*18**0) - (5*18**3 + 7*18**2 + x*18**1 + 1*18**0)
#     f = 1
#     for i in range(2, z//2+1):
#         if z % i == 0:
#             f = 0
#             break
#         else:
#             f = 1
#     if f == 1:
#         c+=1
#         print(x, z)
# print(c)

# print("x y  p")
# for p in range(10, 100):
#     for x in range(1, p):
#         for y in range(1, p):
#             z = (x*p**3 + x*p**2 + x*p**1 + 8*p**0) + (4*p**3 + 3*p**2 + x*p**1 + 9*p**0)
#             h = y*p**3 + y*p**2 + 0*p**1 + 4*p**0
#             if z == h:
#                 print(x,y,p, y*p**2 + y*p**1 + x*p**0)

# 6594
# for x in range(13):
#     z = (7*13**4 + 5*13**3 + 3*13**2 + x*13**1 + 2*13**0) + (2*13**4 + x*13**3 + 1*13**2 + 7*13**1 + 3*13**0)
#     if z % 12 == 0:
#         print(x, z / 12)

# 7616
# for x in range(15):
#     z = (9*15**7 + 7*15**6 + 9*15**5 + 6*15**4 + 8*15**3 + x*15**2 + 1*15**1 + 5*15**0) + \
#         (7*15**4 + x*15**3 + 2*15**2 + 3*15**1 + 3*15**0)
#     if z % 14 == 0:
#         print(z/14, x)

# 7593
# for x in range(15):
#     z = (9*15**7 + 7*15**6 + 9*15**5 + 6*15**4 + 8*15**3 + x*15**2 + 1*15**1 + 3*15**0) + \
#         (7*15**4 + x*15**3 + 2*15**2 + 1*15**1 + 3*15**0)
#     if z % 14 == 0:
#         print(z/14)

# 7816
# for x in range(15):
#     z = (9*15**7 + 7*15**6 + 5*15**5 + 3*15**4 + 1*15**3 + x*15**2 + 1*15**1 + 9*15**0) + \
#         (3*15**4 + x*15**3 + 5*15**2 + 1*15**1 + 9*15**0)
#     if z % 11 == 0:
#         print(z/11)

# for x in range(15):
#     z = (9*15**7 + 7*15**6 + 9*15**5 + 6*15**4 + 8*15**3 + x*15**2 + 1*15**1 + 5*15**0) + \
#         (7*15**4 + x*15**3 + 2*15**2 + 3*15**1 + 3*15**0)
#     if z % 14 == 0:
#         print(z//14, x)

# 8370
# for p in range(10):
#     for q in range(10):
#         if (2*p**2 + 3*p**1 + 4*p**0) == (3*q**2 + 4*q**1 + 5*q**0):
#             print((2*p**2 + 3*p**1 + 4*p**0), (3*q**2 + 4*q**1 + 5*q**0), p, q)

# 8502
# for x in range(15):
#     z = (9*15**7 + 9*15**6 + 6*15**5 + 5*15**4 +
#          8*15**3 + x*15**2 + 2*15**1 + 9*15**0) + (1*15**6 + 0*15**5 + 2*15**4 + x*15**3 + 0*15**2 + 2*15**1 + 3*15**0)
#     if z % 14 == 0:
#         print(z//14, x)

# 8951
# for n in range(15):
#     z = 7**500 - (5*n**1 + 3*n**0)
#     if z % 6 == 0:
#         print(n)

# for x in range(18):
#     z = (7*18**7 + 7*18**6 + 9*18**5 + 6*18**4 + 8*18**3 + x*18**2 + 1*18**1 + 1*18**0) +\
#     (4*18**4 + x*18**3 + 2*18**2 + 1*18**1 + 3*18**0)
#     if z % 7 == 0:
#         print(z//7, x)

# -
# z = 2 * 7**7 + 9 * 7**6 - 44 * 7**3
# for i in range(3000):
#     summ = z+i
#     v7ss = 0
#     while summ > 0:
#         v7ss += summ%7
#         summ //= 7
#     if str(v7ss).count("0") == 0:
#         print(i, v7ss, z)

# ans = []
# for x in range(15):
#     z = (9*15**7 + 7*15**6 + 9*15**5 + 6*15**4 + 8*15**3 + x*15**2 + 1*15**1 + 3*15**0) + \
#     (7*15**4 + x*15**3 + 2*15**2 + 1*15**1 + 3*15**0)
#     if z% 11==0:
#         ans.append(x)
#         print(x)
# print("ans", sum(ans))

# for k in range(4):
#     ss4 = (1*4**6 + 3*4**5 + k*4**4 + k*4**3 + 2*4**2 + 2*4**1 + k*4**0)
#     for l in range(8):
#         ss8 = (1*8**4 + l*8**3 + l*8**2 + 5*8**1 + 0*8**0)
#         for d in range(16):
#             ss16 = (d*16**3 + 12*16**2 + 2*16**1 +  8*16**0)
#             if ss16 == ss8 == ss4:
#                 print(ss16)

# 9369
ans = []
for x in "0123456789ABCDEF":
    xxx = int(f'27A{x}23', 16)
    for y in "0123456789ABCDEF":
        yyy = int(f'8{y}E5D2', 16)
        if (xxx + yyy) % 5 == 0:
            ans.append(int(x, 16) + int(y,16))
print(max(ans))











