# 4711 долгий способ(считает 2 минуты)
# for i in range(1021394, 10**10+1):
#     s = str(i)
#     if s[0] == '1' and s[2:6] == "2139" and s[-1] == "4":
#         if i % 2023 == 0:
#             print(i, i//2023)

# 4711 быстрый способ
# 1021394/2023 = 504,... => 505*2023 = 1021615
# for i in range(1021615, 10**10+1, 2023):
#     s = str(i)
#     if s[0] == '1' and s[2:6] == "2139" and s[-1] == "4":
#         if i % 2023 == 0:
#             print(i, i//2023)

# 4711 через доп. модуль
"""from fnmatch import fnmatch
1021394/2023 = 504,... => 504*2023 = 1019592"""
# import fnmatch
# for i in range(1019592, 10**10+1, 2023):
#     s = str(i)
#     if fnmatch.fnmatch(s, "1?2139*4"):
#             print(i, i//2023)

# 5382 +
# import fnmatch
# for i in range(104200, 10**8+1, 2084):
#     s = str(i)
#     if fnmatch.fnmatch(s, "*1?542?"):
#         print(i, i//2084)

# 4683
# import fnmatch
# for i in range(2123393, 10**8, 37):
#     s = str(i)
#     if fnmatch.fnmatch(s, "2*1234?6"):
#         print(i, i//37)

# 4628
# import fnmatch
# for i in range(123970, 10**8, 161):
#     s = str(i)
#     if fnmatch.fnmatch(s, "12*4?65"):
#         print(i, i//161)

# 4603
# import fnmatch
# for i in range(123375, 10**8, 141):
#     s = str(i)
#     if fnmatch.fnmatch(s, "1234*7"):
#         print(i, i//141)

# 4307
# import fnmatch
# for i in range(123450668, 10**9, 68):
#     s = str(i)
#     if fnmatch.fnmatch(s, "12345?7?8"):
#         print(i, i//68)

# 5678
# import fnmatch
# for i in range(124579, 10**8+1):
#     s = str(i)
#     if fnmatch.fnmatch(s, "124*5*79"):
#         j = sum(int(x) for x in s if int(x) % 2 != 0)
#         if i % j == 0:
#             print(i, sum(int(x) for x in s))

# 5642
# import fnmatch
#
# for i in range(500000, 600000):
#     s = str(i)
#     if fnmatch.fnmatch(s, "*1?3"):
#         maxDel = 0
#         for j in range(1, 500):
#             if i % j == 0:
#                 maxDel = max(maxDel, j)
#         print(i, maxDel)

# import fnmatch
#
# for i in range(1, 10**7):
#     s = str(i)
#     if fnmatch.fnmatch(s, "12?*45"):
#         c = 0
#         maxDel = -10000
#         for j in range(2, 500):
#             if j != i and i % j == 0:
#                 c += 1
#                 maxDel = max(maxDel, j)
#         if c == 18:
#             print(s, maxDel)

# import fnmatch
# rez = []
# for i in range(25, 10**10, 4173):
#     s = str(i)
#     if fnmatch.fnmatch(s, "1?2655*8"):
#         rez.append(s)
# print(rez)

# import fnmatch
# rez = []
# for i in range(345, 10**10, 3013):
#     s = str(i)
#     if fnmatch.fnmatch(s, "1?3948*5"):
#         rez.append(s)
# for i in range(len(rez)):
#     print(rez[i])

# 7625
# import fnmatch
# rez = []
# for i in range(1100456, 10**8):
#     s = str(i)
#     if fnmatch.fnmatch(s, "11??4*56"):
#         if i % 211 == 0:
#             print(s, i//211)

# 7601
# import fnmatch
# for i in range(1200361, 10**8):
#     s = str(i)
#     if fnmatch.fnmatch(s, "12??36*1"):
#         if i % 273 == 0:
#             print(i, i//273)

# 7825
# import fnmatch
# for i in range(1000639, 10**8):
#     s = str(i)
#     if fnmatch.fnmatch(s, "1?0?6*39"):
#         if i % 131 == 0:
#             print(i, i//131)

# import fnmatch
# for i in range(1027110, 10**10, 4891):
#     s = str(i)
#     if fnmatch.fnmatch(s, "1?2711*0"):
#         if i % 4891 == 0:
#             print(i)

# import fnmatch
# for i in range(1200156, 10**8):
#     s = str(i)
#     if fnmatch.fnmatch(s, "12??1*56"):
#         if i % 317 == 0:
#             print(i, i//317)
# 1226156 3868
# 12321156 38868
# 12511356 39468
# 12701556 40068
# 12891756 40668

# 8511
# import fnmatch
# for i in range(1200156, 10**8):
#     s = str(i)
#     if fnmatch.fnmatch(s, "12??15*6"):
#         if i % 253 == 0:
#             print(i, i//253)

# 22
# def f(x):
#     d = set()
#     for i in range(2, int(x**0.5)+1):
#         if x%i == 0:
#             d.add(i)
#             d.add(x//i)
#             # d |= {i, x//i}
#     return sorted(d)
# for i in range(174457, 174506):
#     d = f(i)
#     if len(d) == 2:
#         print(*d)

# import fnmatch
# for i in range(11361, 10**10):
#     s = str(i)
#     if fnmatch.fnmatch(s, "?136*1"):
#         if i%11071 == 0:
#             print(i, i//11071)

# 67
# def f(x):
#     d = set()
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
# for i in range(81234, 134689+1):
#     d = f(i)
#     if len(d) == 3:
#         print(*d)

# 892
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
# for i in range(154026, 154043+1):
#     d = f(i)
#     if len(d) == 4:
#         print(d[2], d[3])

# 1388
# def f(x):
#     d = set()
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
# for i in range(150_001, 150_200):
#     d = f(i)
#     s = sum(d)
#     if s%13 == 10:
#         print(i, s)


# for i in range(130005709, 130005709*100):
#     if i % 999 == 0:
#         print(i)
#         break
# import fnmatch
# for i in range(130005864, 10**9, 999):
#     s = str(i)
#     if fnmatch.fnmatch(s, "13*57?9") and len(s) == 9 and s[1] == "3" and s[-4] == "5":
#         if i % 999 == 0:
#             print(i, i//999)


# import fnmatch
# for i in range(11287139, 11287139*100):
#     if i % 183 == 0:
#         print(i)
#         break
#
# for i in range(11287257, 10**9, 183):
#     s = str(i)
#     if fnmatch.fnmatch(s, "??287*139"):
#         if i % 183 == 0:
#             print(i, i//183)

# 9378
# for i in range(123045679, 123045679*100):
#     if i % 4013 == 0:
#         print(i)
#         break
# import fnmatch
# for i in range(123046606, 10**12, 4013):
#     s = str(i)
#     if fnmatch.fnmatch(s, "123?4*5679"):
#         if i % 4013 == 0:
#             print(i, i//4013)


for i in range(38560, 10**8):
    if i % 768 == 0 and i % 10 != 0:
        print(i)
        break

import fnmatch
for i in range(39168, 10**8, 768):
    s = str(i)
    if fnmatch.fnmatch(s, "38*56?") and (not(fnmatch.fnmatch(s, "38*2*56"))):
        if i % 768 == 0 and i % 10 != 0:
            print(i, i//768)

































