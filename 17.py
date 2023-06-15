"""
№17
with open("*.txt") as f:
    mass = [int(x) for x in f]

maxX = 0
count = 0

for i in range(len(mass) - 1):
    if ((mass[i] + mass[i+1]) % 5 == 0) and ((mass[i] % 3 == 0) or (mass[i+1] % 3 == 0)):
        count += 1
        maxX = max(maxX, mass[i] + mass[i+1])

print(count, maxX)

with open("*.txt") as f:
    mass = [int(x) for x in f]

couter = 0
maxX = -10000
maxPara = -10000
for i in range(len(mass)):
    if mass[i] > maxX and mass[i] % 11 == 0:
        maxX = mass[i]

for i in range(len(mass) - 1):
    if (mass[i] % 11 == 0 or mass[i+1] % 11 == 0) and (mass[i] + mass[i+1] <= maxX):
        couter += 1
        if mass[i] > maxPara:
            maxPara = mass[i]
print(couter, maxPara)

#
with open("*.txt") as f:
    mass = [int(x) for x in f]

xMin = 10000
xSummMax = -10000
counter = 0
for i in range(len(mass)):
    if str(mass[i])[-1] == "7" and mass[i] < xMin:
        xMin = mass[i]

for i in range(len(mass) - 1):
    if (str(mass[i])[-1] == "7" and str(mass[i+1])[-1] != "7") or (str(mass[i])[-1] != "7" and str(mass[i+1])[-1] == "7"):
        a = mass[i]**2 + mass[i+1]**2
        if a < xMin**2:
            counter+=1
            if a > xSummMax:
                xSummMax = a
print(counter,xSummMax)

#KEGE 3579
with open("*.txt") as f:
    m = [int(x) for x in f]

xmax = -1000000000
xmin = 10000000000
counter = 0

for x in m:
    if x % 6 == 0:
        xmin = min(xmin, x)

for i in range(len(m)-1):
    if abs(m[i]) % xmin == 0 and abs(m[i+1]) % xmin == 0:
        counter += 1
        xmax = max(xmax, m[i]+m[i+1])
print(counter, xmax)

#KEGE 4474
with open("*.txt") as f:
    m = [int(x) for x in f]

xmin = 10000000000
xmax = -1000000000
summ = 0
counter = 0
for x in m:
    if x % 103 == 0:
        xmin = min(xmin, x)

for i in range(len(m) - 1):
    if (m[i] + m[i+1]) % 2 == 0:
        if (m[i]-m[i+1]) % xmin == 0:
            counter += 1
            xmax = max(xmax, m[i] + m[i+1])
print(counter, xmax)

#KEGE 2997
with open("*.txt") as f:
    m = [int(x) for x in f]

xmin = 1000000000
summax = -100000000000
counter = 0
mass = []
mass_max = -10000000000
maxmamxmaxmax = 0

for x in m:
    if len(str(x)) == 3:
        mass.append(str(x)[1])

for x in range(0, 9):
    if mass_max < int(m.count(x)):
        mass_max = int(m.count(x))
        maxmamxmaxmax = x

for i in range(len(m) - 1):
    if (str(m[i])[-1] == str(maxmamxmaxmax) or str(m[i+1])[-1] == str(maxmamxmaxmax)):
        counter += 1
        summax = max(summax, m[i]+m[i+1])
print(counter, summax)

#KEGE 2402
with open("*.txt") as f:
    m = [int(x) for x in f]

def ToFrie(peremen):
    print(peremen)
    base = 3
    dop0 = 0
    while peremen >= 0:
        dop0 += peremen % base
        dop0 *= 10
        peremen //= base
    print(dop0, '\n')
    return dop0

counter = 0
mass = []
massmin = []

for i in range(len(m)-2):
    dop1 = ToFrie(m[i])
    dop2 = ToFrie(m[i + 1])
    dop3 = ToFrie(m[i + 2])
    #print(dop1, dop2, dop3)
    if (str(dop1)[-1] == "2") or (str(dop2)[-1] == "2") or (str(dop3)[-1] == "2"):
        counter += 1
        massmin.append(min(m[i], m[i+1], m[i+2]))
print(counter, sum(massmin))        #не решено

#KEGE КИМ № 25014273
with open("*.txt") as f:
    m = [int(x) for x in f]

counter = 0
mMax = -1000000000000

for i in range(len(m)-1):
    if (m[i] + m[i+1]) % 120 == 0:
        counter += 1
        mMax = max(mMax, m[i] + m[i+1])
print(counter, mMax)

#5134

with open("*.txt") as f:
    m = [int(x) for x in f]

xMax = 0
counter = 0
minn = 10000000000

for x in m:
    if (str(x)[-1:-3:-1] == "01") and (xMax < x):
        xMax = x

for i in range(len(m) - 1):
    ost1 = m[i] % 2023
    ost2 = m[i+1] % 2023
    ost = ost2 * ost1
    if ost >= xMax:
        counter += 1
        if ost < minn:
            minn = ost
print(minn, counter)
"""

# 5491 не решил
# with open("*.txt") as f:
#     m = [int(x) for x in f]
#
# c = 0
# xMin = 100000000000
# xMax = -10000000000
# for x in m:
#     if abs(x) % 10 == 3:
#         xMin = min(x, xMin)
#
# for i in range(len(m)-1):
#     if (str(min(m[i], m[i+1]))[-1] == "3") and (m[i]**2 + m[i+1]**2 < xMin**2):
#         c += 1
#         xMax = max(xMax, m[i]**2 + m[i+1]**2)
# print(c, xMax)

# 5672
# with open("*.txt") as f:
#     m = [int(x) for x in f]
#
# massCrat = []
#
# for x in m:
#     if x % 73 == 0:
#         massCrat.append(x)
#
# xCratMax = max(massCrat)
# xMax = -100000000
# c = 0
#
# for i in range(len(m) - 1):
#     if (m[i] >= xCratMax) and (m[i+1] >= xCratMax):
#         c+=1
#         xMax = max(xMax, m[i]+m[i+1])
# print(c, xMax)

# 5635
# with open("*.txt") as f:
#     m = [int(x) for x in f]
#
# mMax = -10000000
# mMin = 10000000
#
# for x in m:
#     mMax = max(mMax, x)
#     mMin = min(mMin, x)
#
# mSumm = abs(mMax + mMin)
# xMaxSumm = -1000000
#
# c = 0
# for i in range(len(m)-1):
#     if m[i] > mSumm and m[i+1] > mSumm:
#         c += 1
#         xMaxSumm = max(xMaxSumm, m[i] + m[i+1])
# print(c, xMaxSumm)

# 5292
# with open("*.txt") as f:
#     m = [int(x) for x in f]
#
# min123 = 100000000
# c = 0
# xMMax = -1000000000
# for x in m:
#     if x % 123 == 0:
#         min123 = min(min123, x)
# # print(min123)
# for i in range(len(m) - 1):
#     if (m[i] % 2023 >= min123 and m[i+1] % 2023 < min123) or (m[i] % 2023 < min123 and m[i+1] % 2023 >= min123):
#         c += 1
#         xMMax = max(xMMax, m[i]+m[i+1])
# print(c, xMMax)

# пробник 30.01 -
# with open("*-1.txt") as f:
#     m = [int(x) for x in f]
#
# srArefm = sum(m) / len(m)
# c=0
# maxSumm = -10000000
#
# for i in range(len(m)-2):
#     if ((m[i] < srArefm) or (m[i+1] < srArefm) or  (m[i+2] < srArefm)) and \
#             (("9" in str(m[i])) or ("9" in str(m[i+1])) or ("9" in str(m[i+2]))):
#         c += 1
#         maxSumm = max(maxSumm, m[i]+m[i+1]+m[i+2])
# print(c, maxSumm)

# with open("*-00.txt") as f:
#     m = [int(x) for x in f]
#
# c=0
# xMax = -10000000
#
# for i in range(len(m)-1):
#     summ1 = sum(int(x) for x in str(m[i]))
#     summ2 = sum(int(x) for x in str(m[i+1]))
#     if (summ2 % 2 == 0 and summ1 % 2 != 0) or (summ2 % 2 != 0 and summ1 % 2 == 0):
#         c+=1
#         xMax = max(xMax, m[i]+m[i+1])
#
# print(c, xMax)

# with open("*.txt") as f:
#     m = [int(x) for x in f]
#
# xMax = -1000000
# xMin = 10000000
# c = 0
#
# for x in m:
#     if str(x)[-1] == '7':
#         xMin = min(xMin, x)
#
# for i in range(len(m)-1):
#     if (str(m[i])[-1] == str(m[i+1])[-1]) and ((m[i] % 7 == 0 and m[i+1] % 7 != 0) or (m[i] % 7 != 0 and m[i+1] % 7 == 0)) and (
#             (m[i]**2 + m[i+1]**2) <= xMin**2):
#         c += 1
#         xMax = max(xMax, m[i]**2 + m[i+1]**2)
# print(c, xMax)

# 2003
# with open("17.txt") as f:
#     m = [int(x) for x in f]
# c = 0
# xMax = -100000
# for x in m:
#     if (x % 3 == 0) and (x % 7 != 0) and (x % 17 != 0) and (x % 19 != 0) and (x % 27 != 0):
#         c += 1
#         xMax = max(xMax, x)
#
# print(c, xMax)

# 2015
# with open("*.txt") as f:
#     m = [int(x) for x in f]
# ans = []
# for x in m:
#     if ((str(x)[-1] == "5") or (str(x)[-1] == "7")) and ((x % 9 != 0) and (x % 11 != 0)):
#         ans.append(x)
# print(len(ans), min(ans)+max(ans))

# 6605
# with open("*.txt") as f:
#     m = [int(x) for x in f]
#
# xMax = -100000
# xMin = 100000
# c = 0
#
# for x in m:
#     if str(x)[-1] == "5":
#         xMax = max(xMax, x)
#
# for i in range(len(m)-1):
#     if (((str(m[i])[-1] == '5') and (str(m[i+1])[-1] != '5')) or ((str(m[i])[-1] != '5') and (str(m[i+1])[-1] == '5'))) \
#         and (abs(m[i]**2 - m[i]**2) <= xMax**2):
#         xMin = max(abs(m[i]**2 - m[i]**2), xMin)
#         c += 1
# print(c, xMin)

# kPolykov 245
# with open("17-243.txt") as f:
#     m = [int(x) for x in f]
# c = 0
# mx = 10000
# max71 = 0
# for x in m:
#     if x % 71 == 0:
#         max71 = max(max71, x)
#
# for i in range(len(m)-1):
#     if ((m[i] < max71) and (m[i+1] < max71)) and ((m[i] % 13 == 0) or (m[i+1] % 13 == 0)):
#         c += 1
#         mx = min(mx, m[i]+m[i+1])
# print(c, mx)

# kPolykov 268
# m = [int(x) for x in open("17-243.txt").readlines()]
# c = 0
# mx = 10000
# sx = 0
# for x in m:
#     if x % 49 == 0:
#         sx += sum(int(z) for z in str(x))
#
# for i in range(len(m)-1):
#     if ((m[i] > sx) and (m[i+1] <= sx) and (str(m[i+1])[-1] == "7")) or \
#         ((m[i+1] > sx) and (m[i] <= sx) and (str(m[i])[-1] == "7")):
#         c += 1
#         mx = min(mx, m[i]+m[i+1])
# print(c, mx)

# 2013
# m = [int(x) for x in open("files17/17_2013.txt").readlines()]
# c=0
# xMax = 10000
# for i in range(len(m)-1):
#     if ((m[i] % 10 == 2) or (m[i]%10 == 7)) and (m[i]%3 == 0) and (m[i]%11 == 0):
#         c += 1
#         xMax = min(xMax,m[i])
# print(c, xMax)

# 2016
# m = [int(x) for x in open("files17/17_2016.txt").readlines()]
# c = 0
# xMin = 10000
# xMax = 0
# for x in m:
#     if x%13 == 7 and x%7!=0 and x%11 != 0:
#         c += 1
#         xMin = min(xMin, x)
#         xMax = max(xMax,x)
# print(c, xMax-xMin)

# 2017
# m = [int(x) for x in open("files17/17_2017.txt").readlines()]
# c = 0
# ans = []
# for x in m:
#     if (hex(x)[-1] == "b") and ((x % 7 == 0) and (x % 6 != 0) and (x % 13 != 0) and (x % 19 != 0)):
#         c += 1
#         ans.append(x)
# print(sum(ans), c)

# 1993
# m = [int(x) for x in open("files17/17_1993.txt").readlines()]
# c = 0
# xMax = -10000
# for i in range(len(m)-1):
#     if ((m[i]+m[i+1])%3 == 0) and ((m[i]+m[i+1])%6 != 0) and (str(m[i]*m[i+1])[-1] == "8"):
#         c += 1
#         xMax = max(m[i]+m[i+1], xMax)
# print(c, xMax)

# 1994
# m = [int(x) for x in open("files17/17_1994.txt").readlines()]
# c = 0
# xMin = 10000000000000000
# ans = []
# for i in range(len(m)-1):
#     if (m[i]*m[i+1] > 0) and ((m[i]+m[i+1])%7 == 0):
#         c += 1
#         xMin = min(m[i]*m[i+1], xMin)
#         ans.append(m[i]*m[i+1])
# print(c, min(ans), xMin)

# 1998
# m=[int(x) for x in open("files17/17_1998.txt").readlines()]
# c = 0
# ans = []
# for i in range(len(m)-2):
#     if ((m[i]*m[i+1]*m[i+2])%7 == 0) and (str(m[i]+m[i+1]+m[i+2])[-1]=="5"):
#         c += 1
#         ans.append(m[i]+m[i+1]+m[i+2])
# print(c, max(ans))

# 1999
# m = [int(x) for x in open("files17/17_1999.txt").readlines()]
# c = 0
# ans = []
# for i in range(len(m)-2):
#     if ((m[i]%12 == 0) or (m[i+1]%12 == 0) or (m[i+2]%12 == 0)) and ((m[i]%3 == 0) and (m[i+1]%3 == 0) and (m[i+2]%3 == 0)):
#         c += 1
#         ans.append((m[i]+m[i+1]+m[i+2])/3)
# print(c, min(ans))

# 2402
# m = [int(x) for x in open("files17/17_2402.txt").readlines()]
# c=0
# ans = []
# for i in range(len(m)-2):
#     if ((m[i]%3 == 2) or (m[i+1]%3 == 2) or (m[i+2]%3 == 2)):
#         c+=1
#         ans.append(min(m[i],m[i+1],m[i+2]))
# print(c, sum(ans))

# 2002
# m = [int(x) for x in open("files17/17_2002.txt").readlines()]
# c = 0
# xMin = 10000
# for i in range(len(m)-2):
#     if (m[i]>m[i + 1]>m[i + 2]>m[i + 3]) and (m[i]-m[i+3] > 1000):
#         c += 1
#         xMin = min(xMin, m[i]+m[i+1]+m[i+2]+m[i+3])
# print(c, xMin)

# 2400
# m = [int(x) for x in open("files17/17_2400.txt").readlines()]
# c = 0
# xMax = -10000
# for i in range(len(m)-1):
#     if (m[i]+m[i+1]>100) and ((m[i]< 0) or (m[i+1]<0)):
#         c += 1
#         xMax = max(xMax, m[i]*m[i+1])
# print(c, xMax)

# 2238
# m = [int(x) for x in open("files17/17_2238.txt").readlines()]
# c = 0
# srZnach = sum(m) / len(m)
# xMax = -10000
# for i in range(len(m) - 2):
#     dopCount = 0
#     if m[i] > srZnach:
#         dopCount += 1
#     if m[i + 1] > srZnach:
#         dopCount += 1
#     if m[i + 2] > srZnach:
#         dopCount += 1
#     if dopCount >= 2:
#         c += 1
#         xMax = max(xMax, m[i]+m[i+1]+m[i+2])
# print(c, xMax)

# 2239
# m = [int(x) for x in open("files17/17_2239.txt").readlines()]
# c = 0
# xMin = 10000000000
# xMax = 0
# for x in m:
#     if x % 19 == 0:
#         xMax = max(x, xMax)
# for i in range(len(m)-1):
#     if (m[i] > xMax or m[i+1]>xMax):
#         c += 1
#         xMin = min(xMin, m[i]+m[i+1])
# print(c, xMin)

# 2309
# m = [int(x) for x in open("files17/17_2309.txt").readlines()]
# crat11 = []
# ans17 = []
# for x in m:
#     if x % 17 == 0:
#         ans17.append(x)
#     if x % 11 == 0:
#         crat11.append(x)
# if len(crat11) > len(ans17):
#     print("11", len(crat11), min(crat11))
# else:
#     print("17", len(ans17), max(ans17))

# 2310
# m = [int(x) for x in open("files17/17_2310.txt").readlines()]
# c = 0
# xMax = 0
# xMin = 100000
# for x in m:
#     if str(x)[-1] == "4":
#         xMax = max(x, xMax)
#         xMin = min(x, xMin)
# xSumm = xMin + xMax
# SummMax = 0
# for i in range(len(m)-1):
#     if (m[i]+m[i+1] < xSumm):
#         c += 1
#         SummMax = max(SummMax, m[i]+m[i+1])
# print(c, SummMax)

# 2403
# m = [int(x) for x in open("files17/17_2403.txt").readlines()]
# c = 0
# xMax = -10000000000
# for i in range(len(m)-1):
#     if ((m[i] % 9 == 0) and (oct(m[i+1])[-1] == '3') and (m[i+1] % 9 != 0)) or ((m[i+1] % 9 == 0) and (oct(m[i])[-1] == '3') and (m[i] % 9 != 0)):
#         c += 1
#         xMax = max(xMax, m[i], m[i+1])
# print(c, xMax)

# 2398
# m = [int(x) for x in open("files17/17_2398.txt").readlines()]
# summMax = -100000000
# c = 0
# for i in range(len(m)-2):
#     if not(m[i] > 0 and str(m[i])[-1] == '9') and (m[i+1] > 0 and str(m[i+1])[-1] == '9') and not(m[i+2] > 0 and str(m[i+2])[-1] == '9'):
#         c += 1
#         summMax = max(summMax, m[i]+m[i+1]+m[i+2])
# print(c, summMax)

# 2399
# m = [int(x) for x in open("files17/17_2399.txt").readlines()]
# c = 0
# summ35 = 0
# for x in m:
#     if x % 35 == 0:
#         summ35 += sum(int(y) for y in str(x))
# xMin = 10000000
# for i in range(len(m)-1):
#     if ((m[i] > summ35) and not(m[i+1] > summ35) and (hex(m[i+1])[-2:] == 'ef')) \
#         or (not(m[i] > summ35) and (m[i+1] > summ35) and (hex(m[i])[-2:] == 'ef')):
#         c += 1
#         xMin = min(xMin,m[i]+m[i+1])
# print(c, xMin)

# m = [int(x) for x in open("*.txt").readlines()]
# lastElement = 0
# for x in m:
#     if str(x)[-1] == str(x)[-2]:
#         lastElement = min(lastElement, x)
# c = 0
# kvSummMax = -10000000000
# for i in range(len(m)-1):
#     if ((str(m[i])[-1] == str(m[i+1])[-2]) or (str(m[i])[-2] == str(m[i+1])[-1]))and \
#         (((m[i]%13 == 0) and (m[i+1]%13 != 0)) or ((m[i+1]%13 == 0) and (m[i]%13 != 0))) and \
#             (m[i]**2 + m[i+1]**2 <= lastElement**2):
#         c += 1
#         kvSummMax = max(kvSummMax, m[i]**2 + m[i+1]**2)
# print(c, kvSummMax)

# 7619
# with open("17_7619.txt") as f:
#     m = [int(x) for x in f]
#
# c=0
# xMax = -100000
# xMin = -1000000
# for x in m:
#     if len(str(x)) == 2:
#         xMax = max(xMax, x)
#
# for i in range(len(m)-1):
#     if ((len(str(m[i])) == 2 and len(str(m[i+1])) != 2) or (len(str(m[i+1])) == 2 and len(str(m[i])) != 2)) and \
#         ((m[i] + m[i+1])%xMax == 0):
#         c += 1
#         xMin = max(xMin, m[i] + m[i+1])
# print(c, xMin)

# 7596
# with open("17_7596.txt") as f:
#     m = [int(x) for x in f]
# c = 0
# xMin = 1000000
# xMax = 10000000
# for x in m:
#     if len(str(x)) == 3 and str(x)[-1] == '5':
#         xMin = min(xMin, x)
# for i in range(len(m)-1):
#     if (((len(str(m[i])) == 3) and (len(str(m[i+1])) != 3)) or ((len(str(m[i])) != 3) and (len(str(m[i+1])) == 3))) and \
#             ((m[i] + m[i+1])% xMin == 0):
#         c +=1
#         xMax = min(m[i] + m[i+1], xMax)
# print(c, xMax)
#
# # 7596
# a = [int(x) for x in open("17_7596.txt")]
# min3 = min([x for x in a if 100<= x <= 999 and x %10==5])
# ans = []
#
# for i in range(len(a)-1):
#         if ((len(str(a[i])) == 3 and len(str(a[i+1])) != 3) or (len(str(a[i])) != 3 and len(str(a[i+1])) == 3)) \
#                 and ((a[i] + a[i + 1]) % min3 == 0):
#                 ans.append(a[i] + a[i+1])
# print(len(ans),min(ans))

# from colorama import init, Fore
#
# init(autoreset=True)
# print(Fore.RED + 'some red text')
# print('automatically back to default color again')

# 7819
# with open("files/17_7819.txt") as f:
#     m = [int(x) for x in f]
# c = 0
# xMin = -1000000
# xMaxBvuznach = -1000000
# for x in m:
#     if len(str(x)) == 2:
#         xMaxBvuznach = max(x, xMaxBvuznach)
# for i in range(len(m)-1):
#     if ((m[i] > 0 and len(str(m[i])) == 3) or (m[i+1] > 0 and len(str(m[i+1])) == 3)) and \
#         ((m[i] + m[i+1]) % xMaxBvuznach == 0):
#         c += 1
#         xMin = max(xMin, m[i] + m[i+1])
# print(c, xMin)

# with open("*.txt") as f:
#     m = [int(x) for x in f]
# c = 0
# xMin = 1000000
# xMax = -1000000
# for x in m:
#     if len(str(x)) == 3 and str(x)[-1] == '5':
#         xMin = min(xMin, x)
# for i in range(len(m)-1):
#     if (((len(str(m[i])) == 4) and (len(str(m[i+1])) != 4)) or ((len(str(m[i])) != 4) and (len(str(m[i+1])) == 4))) and \
#             ((m[i]**2 + m[i+1]**2)%xMin == 0):
#         c += 1
#         xMax = max(xMax, m[i]+m[i+1])
# print(c, xMax)

# with open("1_17.txt") as f:
#     m = [int(x) for x in f]
# c = 0
# xMin = -1000000
# xMax = -1000000
# for x in m:
#     if len(str(x)) == 2:
#         xMax = max(x, xMax)
# for i in range(len(m)-1):
#     if (((len(str(m[i])) == 2) and (len(str(m[i+1])) != 2)) or ((len(str(m[i])) != 2) and (len(str(m[i+1])) == 2))) and \
#             (m[i] + m[i+1]) % xMax == 0:
#         c += 1
#         xMin = max(xMin, m[i] + m[i+1])
# print(c, xMin)

# 8373
# m = [int(x) for x in open("17_8373.txt").readlines()]
# c = 0
# kratMinChet = minSumm = 1000000
# for x in m:
#     if x % 2 == 0:
#         kratMinChet = min(x, kratMinChet)
# for i in range(len(m)-2):
#     if ((m[i]%2 == 0 and m[i+2]%2 != 0) or (m[i]%2 != 0 and m[i+2]%2 == 0)) and m[i+1] % kratMinChet == 0:
#         c += 1
#         minSumm = min(minSumm, m[i]+m[i+2])
# print(c, minSumm)

# 8504
# with open("17_8504.txt") as f:
#     m = [int(x) for x in f]
#
# minCrat = 100000000
# maxSumm = -10000
# c = 0
# for x in m:
#     if len(str(x)) == 3 and str(x)[-1] == "5":
#         minCrat = min(minCrat, x)
# for i in range(len(m)-1):
#     if ((len(str(m[i])) == 3) or (len(str(m[i+1])) == 3)) and ((m[i] + m[i+1]) % minCrat == 0):
#         c+=1
#         maxSumm = max(maxSumm, (m[i] + m[i+1]))
# print(c, maxSumm)

# 8954
# with open("17_8954.txt") as f:
#     m = [int(x) for x in f]
#
# maxCrat16 = -100000
# for x in m:
#     if hex(x)[-2:] == "0f":
#         maxCrat16 = max(maxCrat16, x)
#
# c = 0
# maxSumm = -10000
# for i in range(len(m)-1):
#     if (((m[i] % 7 == 0) and (m[i+1] % 7 != 0)) or ((m[i] % 7 != 0) and (m[i+1] % 7 == 0))) and \
#         ((m[i] + m[i+1]) % maxCrat16 == 0):
#         c+=1
#         maxSumm = max(maxSumm, m[i]+m[i+1])
# print(c, maxSumm)

# with open("17.txt") as f:
#     m = [int(x) for x in f]
# allSumm = 0
# for x in m:
#     allSumm += sum(int(j) for j in str(x))
# c = 0
# xMin = 1000000000
# for i in range(len(m)-1):
#     if (((str(m[i])[-2:] == "10") and (str(m[i+1])[-2:] != "10")) or ((str(m[i])[-2:] != "10") and (str(m[i+1])[-2:] == "10"))) and \
#             (allSumm > m[i]+m[i+1]):
#         c += 1
#         xMin = min(xMin, m[i+1] + m[i])
# print(c, xMin)

# with open("17.txt") as f:
#     m = [int(x) for x in f]
# minx4 = 10000000
# for x in m:
#     if len(str(x)) == 4 and x%7 == 0 and x > 0:
#         minx4 = min(minx4, x)
# c = 0
# xMin = 100000000000000000000
# for i in range(len(m)-1):
#     if (len(str(abs(m[i]))) + len(str(abs(m[i+1]))) == 6) and (str(m[i])[-1] == str(m[i+1])[-1]) and \
#            ((m[i]**2 + m[i+1]**2) > minx4**2):
#         c += 1
#         xMin = min(xMin, m[i]**2 + m[i+1]**2)
# print(c, xMin)

# with open("17.txt") as f:
#     m = [int(x) for x in f]
# maxLen3 = -1
# for x in m:
#     if len(str(x)) == 3:
#         maxLen3 = max(maxLen3, x)
# c=0
# xMin = 100000000000000000
#
# for i in range(len(m)-1):
#     if ((len(str(m[i])) == 3 and len(str(m[i+1])) != 3) or (len(str(m[i])) != 3 and len(str(m[i+1])) == 3)) and \
#             ((m[i] * m[i+1]) % maxLen3 == 0):
#         c += 1
#         xMin = min(m[i] * m[i+1], xMin)
# print(c, xMin)

# with open("17.txt") as f:
#     m = [int(x) for x in f]
# dvizMin = 100000000
# for x in m:
#     if len(str(abs(x))) == 2 and str(x)[-1] == "1":
#         dvizMin = min(x, dvizMin)
# c = 0
# xMin = 1000000
# for i in range(len(m)-1):
#     if ((m[i]**2 < dvizMin**2) and (m[i+1]**2 >= dvizMin**2)) or \
#             ((m[i]**2 >= dvizMin**2) and (m[i+1]**2 < dvizMin**2)):
#         c += 1
#         xMin = min(xMin, m[i]+m[i+1])
# print(c, xMin)
#

# 9372
# with open("17_9372.txt") as f:
#     m = [int(x) for x in f]
# xCratMax = -10000
# for x in m:
#     if abs(x) % 1001 == 0:
#         xCratMax = max(xCratMax, x)
# c = 0
# xMin = 10000000
# for i in range(len(m)-1):
#     if (len(str(abs(m[i]))) == 3 or len(str(abs(m[i+1]))) == 3) and ((m[i] + m[i+1]) > xCratMax):
#         c += 1
#         xMin = min(xMin, m[i]+m[i+1])
# print(c, xMin)


with open("17.txt") as f:
    m = [int(x) for x in f]
xMax3Ceat = -10000
for x in m:
    if len(str(abs(x))) == 3 and x > 0:
        xMax3Ceat = max(xMax3Ceat, x)
c = 0
xMaxSumm = -1
for i in range(len(m)-1):
    if ((len(str(m[i])) == 3  and len(str(m[i+1])) != 3) or (len(str(m[i])) != 3  and len(str(m[i+1])) == 3)) and \
            ((m[i] + m[i+1]) % xMax3Ceat == 0):
        c += 1
        xMaxSumm = max(xMaxSumm, m[i]+m[i+1])
print(c, xMaxSumm)























