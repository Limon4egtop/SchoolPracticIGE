"""#34517

for A in range(100):
    flag = 1
    for x in range(100):
        if (x & A != 0) <= ((x&10 == 0) <= (x&3 != 0)):
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(A)

#33094

for A in range(1, 200):
    flag = 1
    for x in range(1, 200):
        if (A < 50) and ((x % A != 0)) <= ((x % 10 == 0) <= (x % 18 != 0)):
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(A)

#13745
for A in range(1, 1000):
    flag = 1
    for x in range(1, 200):
        for y in range(1, 200):
            if ((x <= 9) <= (x*x <= A)) and ((y*y <= A) <= (y <= 9)):
                flag = 1
            else:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        print(A)

#15928
for a1 in range(-10, 100):
    for a2 in range(a1+1, 101):
        flag = 1
        for x in range(-100, 200):
            for y in range(-100, 200):
                if ((a1 <= x <= a2) <= (x ** 2 <= 81)) and ((y ** 2 <= 36) <= (a1 <= y <= a2)):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 0:
                break
        if flag == 1:
            print(a1, a2)       #ответ [ -9;9]

#KEGE КИМ № 25014273
summ = 0
for A in range(1, 101):
    flag = 1
    for x in range(1, 200):
        for y in range(1, 200):
            if ((x+y) <= 22) or (y <= (x-6)) or (y>= A):
                flag = 1
            else:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        summ += A
print(summ)

#Kege 757
for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        if (((x % a ==   0) and (x % 21 == 0)) <= (x % 18 == 0)) == False:
            flag = False
            break
    if flag:
        print(a)
        break

#KEGE 759
for A in range(1, 1000):
    flag = 0
    for x in range(1, 1000):
        if ((x % A == 0) and (x % 50 != 0)) <= ((x % 18 != 0) or (x % 50 == 0)):
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(A)
        break

#KEGE 2080 23.11 +
for A in range(1,100):
    f = 1
    for x in range(1,100):
        for y in range(1,100):
            if (((x**2 - 10*x + 16) > 0) or ((y**2 - 10*y + 21) > 0) or ((x*y) < (2*A))):
                f = 1
            else:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)

#KEGE 4675 23.11 +
for A in range(1, 100):
    f = 1
    for x in range(1,100):
        if ((x % 6 == 0) <= (x % 10 != 0)) or (x + A > 121):
            f = 1
        else:
            f = 0
            break
    if f == 1:
        print(A)

#KEGE 2079 23.11 +
for A in range(1,100):
    f = 1
    for x in range(1, 100):
        if (x&107 == 0) <= ((x&55 != 0) <= (x&A != 0)):
            f = 1
        else:
            f = 0
            break
    if f == 1:
        print(A)

#KEGE 1773 23.11 +
for A in range(1,300):
    f = 1
    for x in range(1,300):
        for y in range(1,300):
            if ((x < A) and (y < A) and (x*y > 1200)) == 0:
                f = 1
            else:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)

#KEGE 829 23.11 +
for A in range(-100, 100):
    f = 1
    for x in range(1, 100):
        for y in range(1, 100):
            if (y > 7 - 2*x) or ((2 * (x + A)) >= ((y - A) ** 2)):
                f = 1
            else:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)

#KEGE 1126 23/11 +
counter = 0
for A in range(1, 1001):
    f = 1
    for x in range(1,1001):
        if (A % 35 == 0) and (730 % x == 0) <= ((A % x != 0) <= (110%x != 0)):
            f = 1
        else:
            f = 0
            break
    if f == 1:
        print(A)
        counter+=1
print("\n"*4, counter)

#723
for A in range(1, 1001):
    f = 1
    for x in range(1, 1001):
        if ((x % 34 == 0) and (x % 51 != 0)) <= ((x % A != 0) or (x % 51 == 0)):
             f = 1
        else:
            f = 0
            break
    if f == 1:
        print(A)

#59
for A in range(1,1000):
    flag = 1
    for x in range(1, 1000):
        f = ((x % A == 0) and (x % 24 == 0) and (x%16 != 0)) <= (x % A != 0)
        if f == 1:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(A)

#432
def f(a,x):
    return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)

for a in range(1,3000):
    if all(f(a,x)==1 for x in range(1,30000)):
        print(a)

#764
def f(A, x):
    return ((x % 15 == 0) and (x%21!= 0)) <= ((x%A != 0) or (x%15!=0))

for A in range(1,10000):
    if all(f(A,x) == 1 for x in range(1,9000)):
        print(A)
        break

#948
def f(A, x):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != A)

for A in range(1,300):
    if all(f(A, x) == 1 for x in range(1, 3000)):
        print(A)

#1127
def f(A, x):
    return (A % 7 == 0) and ((240 % x == 0) <= ((A % x != 0) <= (780 % x != 0)))

for A in range(1, 1000):
    if all(f(A, x) == 1 for x in range(1,3000)):
        print(A)

#216
def f(A, x):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & A != 0))

for A in range(1,500):
    if all(f(A,x) == 1 for x in range(1,1000)):
        print(A)
        break

#2078
def f(A, x):
    return (((x & 13 != 0) or (x & A != 0)) <= (x & 13 != 0)) or ((x & A != 0) and (x & 39 == 0))

for A in range(1,500):
    if all(f(A, x) == 1 for x in range(1,1000)):
        print(A)

#2079
def f(A,x):
    return (x & 107 == 0) <= ((x & 55 != 0) <= (x & A != 0))

for A in range(1,1000):
    if all(f(A,x) == 1 for x in range(1,1000)):
        print(A)
        break

#2081

#627
def func(x, y, A):
    return (x * y > A) and (x > y) and (x < 8)

for A in range(1, 1000):
    f = 0
    for x in range(1, 500):
        for y in range(1, 500):
            if func(x,y,A) == 0:
                f = 1
            else:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)
        break

#1015
def func(x, y, A):
    return (x > 39) or (y > 26) or (2*x + 4*y < A)

for A in range(1,500):
    f = 1
    for x in range(1,500):
        for y in range(1, 500):
            if func(x, y, A) == 1:
                f = 1
            else:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)

#1859
def func(x, y, A):
    return (2*x + y != 70) or (x < y) or (A < x)

for A in range(1, 1000):
    f = 1
    for x in range(1,500):
        for y in range(1, 500):
            if func(x, y, A) == 1:
                f = 1
            else:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)
"""
#2080
# def funk(x, y, A):
#     return (x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2*A)
#
# for A in range(1, 1000):
#     f = 1
#     for x in range(1, 500):
#         for y in range(1, 500):
#             if funk(x, y, A) == 1:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(A)
#         break

# 5368 -
# for A in range(1, 100):
#     f = 1
#     for x in range(1, 500):
#         f = (x % 17 == 0) <= (x % 53 != 0) or (not(A < 90000000-x))
#         if f == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(A)

# 5671
# for A in range(1,300):
#     f = 1
#     for x in range(1,400):
#         g = (x + A >= 160) or ((x % 7 == 0) <= (not(x + (-17) > 0)))
#         if g == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(A)

# 5633
# for A in range(1, 1000):
#     f = 1
#     for x in range(1, 500):
#         z = ((x % 3 == 0) <= (x % 17 != 0)) or (not(A < 190 - x))
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(A)

# 5290
# for A in range(1,1000):
#     f = 1
#     for x in range(1,500):
#         for y in range(1, 500):
#             z = not((x+5 < A) <= (y > A)) or (x*y >= 76)
#             if z == 1:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(A)

# 4282
# def f(a,x,y,z):
#     return (150 != y + 2*x + 2*z) or (a < x) or (a < y) or (a < z)
#
# for a in range(100):
#     if all(f(a,x,y,z) for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
#         print(a)        #ответ 29

# 1968
# def f(a1, a2, x):
#     return (170 <= x <= 580) <= ((not(290 <= x <= 800) and
#                                 (not(a1*10 <= x <= a2*10))) <= (not((170 <= x <= 580))))
#
# rez = []
#
# for a1 in range(0, 100):
#     for a2 in range(a1+1, 100+1):
#         if all(f(a1,a2,x) for x in range(1000)):
#             rez.append(a2-a1)
# print(min(rez))

# 1440
# def f(a1, a2, x):
#     return ((120 <= x <= 280) <= (a1*10 <= x <= a2*10)) and (not(150 <= x <= 300) or (a1*10 <= x <= a2*10))
#
# rez = []
#
# for a1 in range(100):
#     for a2 in range(a1+1, 100+1):
#         if all(f(a1, a2, x) for x in range(1000)):
#             rez.append(a2-a1)
# print(min(rez))

# 1370 -
# def f(a1, a2, x):
#     return ((200 <= x <= 850) == (300 <= x <= 650)) <= (not(a1*10 <= x <= a2*10))
# rez2 = []
# for a1 in range(100):
#     for a2 in range(a1+1, 100+1):
#         if all(f(a1,a2,x) for x in range(1000)):
#             rez2.append(a2-a1)
#
# print(min(rez2))

# -
# def f(a1, a2, x):
#     return ((2950 <= x <= 4000) <= (50 <= x <= 2800)) or (not(a1*10 <= x <= a2*10) <= (3750 <= x <= 4500))
# rez = []
# for a1 in range(1, 1000):
#     for a2 in range(1, 1000):
#         if all(f(a1,a2,x) for x in range(1, 10000)):
#             rez.append(a2-a1)
# print(min(rez))

# def kon(x1, x2):
#     c = ""
#     z1 = bin(x1)[2:]
#     z2 = bin(x2)[2:]
#     if len(z1) > len(z2):
#         z2 = "0"*(len(z1)-len(z2)) + z2
#     if len(z2) < len(z2):
#         z1 = "0"*(len(z2)-len(z1)) + z1
#     while z1 != "":
#         if z1

# 6595
# for A in range(1, 1000):
#     f = 1
#     for x in range(1, 1000):
#         z = ((x%3 == 0) <= (x % 2 != 0)) or (x-A >= 4)
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(A)

# for a in range(1, 100):
#     f = 1
#     for x in range(100):
#         z = ((x&116 != 0) or (x&92 != 0)) <= ((x&69 == 0) <= (x&a != 0))
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(a)

# for a in range(1, 1000):
#     f = 1
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             z = (x >= 9) or (2*x < y) or (x*y < a)
#             if z:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(a)

# REGE 7763
# def f(a1,a2,x):
#     return ((50 <= x <= 300) == (140 <= x <= 230)) <= (not(a1 <= x <= a2))
# rez = []
# for a1 in range(40, 320):
#     for a2 in range(a1+1, 330):
#         if all(f(a1,a2, x) for x in range(4, 440)):
#             rez.append((a2-a1)/10)
# print(max(rez))
# print(round(max(rez)))

# def f(a1,a2, x):
#     return (1300 <= x <= 1710) <= (((1500 <= x <= 1850) and (not(a1 <= x <= a2))) <= (not(1300 <= x <= 1710)))
#
# rez = []
# for a1 in range(1290, 1870):
#     for a2 in range(a1+1, 1880):
#         if all(f(a1,a2,x) for x in range(1290,1880)):
#             rez.append(a2-a1)
# print(min(rez)/10)

# 4286
# def f(a1,a2,x):
#     return (250<=x<=420) <= (not(10 <= x <= 980) and (250<=x<=420) <= (a1 <= x <= a2))
#
# rez = []
# for a1 in range(0, 1000):
#     for a2 in range(a1+1, 1010):
#         if all(f(a1,a2,x) for x in range(0,1010)):
#             rez.append(a2-a1)
# print(rez)
# print(min(rez)/10)      #ответ 0

# 307
# def f(a1,a2,x):
#     return ((30 <= x <= 150) == (140<= x <= 250)) <= (not(a1<=x<=a2))
#
# rez = []
# for a1 in range(20, 270):
#     for a2 in range(a1+1, 280):
#         if all(f(a1,a2,x) for x in range(20, 280)):
#             rez.append(a2-a1)
# print(max(rez)/10)

# 1295
# def f(a1,a2,x):
#     return (170 <= x <= 540) <= (((370 <= x <= 830) and (not(a1 <= x <= a2))) <= (not(170 <= x <= 540)))
# rez = []
# for a1 in range(170, 850):
#     for a2 in range(a1+1, 860):
#         if all(f(a1,a2,x) for x in range(170, 860)):
#             rez.append(a2-a1)
# print(min(rez)/10)

# 7453
# def f(a,x):
#     return (x % a == 0) or ((70 <= x <= 80) <= (not(x%18 == 0)))
# rez = []
# for a in range(1, 300):
#     z = 1
#     for x in range(1, 500):
#         if f(a, x) == 1:
#             z = 1
#         else:
#             z = 0
#             break
#     if z == 1:
#         rez.append(a)
# print(len(rez))

# 7594
# print(14&5)
# for a in range(1, 50):
#     f = 1
#     for x in range(1, 100):
#         z = (x&39 == 0) or ((x&11 == 0) <= (not(x&a == 0)))
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(a)

# 7817
# def f(a, x):
#     return ((x % 13 == 0) <= (not(40 <= x <= 60))) or (a < x + 20)
# rez = []
# for a in range(1, 1000):
#     if all(f(a, x) for x in range(1, 302)):
#         rez.append(a)
# print(max(rez))

# def f(x, a1, a2):
#     return (not((190 <= x <= 800) <= ((130 <= x <= 310) or (480 <= x <= 1140)))) <= (not(a1 <= x <= a2) <= (not(190 <= x <= 800)))
# ans = []
# for a1 in range(120, 1160):
#     for a2 in range(a1+1, 1170):
#         if all(f(x, a1, a2) for x in range(10, 1170)):
#             ans.append(a2-a1)       #16.8 => 17
# print(min(ans), ans)

# for a in range(1, 400):
#     f = 1
#     for x in range(1, 500):
#         for y in range(1, 500):
#             z = (x >= 12) or (3*x < y) or (x*y < a)
#             if z:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(a)

# for a in range(1, 1000):
#     f = 1
#     for x in range(1, 101):
#         for y in range(1, 102):
#             z = (11 <= y) or (7*y < x) or (a > x*y)
#             if z == 1:
#                 f = 1
#             else:
#                 f = 0
#                 break
#         if f == 0:
#             break
#     if f == 1:
#         print(a)

# 8503
# for A in range(1, 100):
#     f = 1
#     for x in range(1, 200):
#         z = ((x & 52 != 0) and (x&36 == 0)) <= (not(x&A == 0))
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(A)

# 8952
# print(14&5 == 0)
# for a in range(1, 100000000000000):
#     f = 1
#     for x in range(1, 200):
#         z = (x&103 == 0) and (x&94 != 0) <= (x&a != 0)
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(a)

# for a in range(1, 50):
#     f = 1
#     for x in range(15,30+1):
#         z = (x&29 == 0) or ((x&11 == 0) <= (x&a != 0))
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f == 1:
#         print(a)

# for a in range(1, 100):
#     f = 1
#     for x in range(1, 300):
#         z = ((x % 5 == 0) <= (x % 7 != 0)) or (not(x+a <= 120))
#         if z == 1:
#             f = 1
#         else:
#             f = 0
#             break
#     if f:
#         print(a)



























