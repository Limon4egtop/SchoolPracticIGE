# 2719 A
# f = open("files_27_1/27A_2719.txt")
# n = int(f.readline())
# m = [int(x) for x in f.readlines()]
# k=0
# for i in range(n):
#     for j in range(i+1,n):
#         if (m[i]+m[j])%2 == 0:
#             k += 1
# print(k)  #2459
# B
# f = open("files_27_1/27B_2719.txt")
# n = int(f.readline())
# k0, k1 = 0, 0
# for i in range(n):
#     x = int(f.readline())
#     if x%2==0: k0 += 1
#     else: k1 += 1
# print(k0*(k0 - 1)//2 + k1*(k1 - 1)//2)

# 2720 A
# import itertools
# f = open("files_27_1/27A_2720.txt")
# n = int(f.readline())
# m = [int(x) for x in f.readlines()]
# c=0
# for x,y in itertools.combinations(m, 2):
#     if x*y%7 == 0:
#         c+=1
# print(c)        #1209
# B
# f = open("files_27_1/27B_2720.txt")
# n = int(f.readline())
# k7 = k0 = 0
# for i in range(n):
#     x = int(f.readline())
#     if x%7==0:
#         k7 += 1
#     else:
#         k0 += 1
# print(k7*(k7-1)//2 + k7*k0)

# 2721 a
# import itertools
# f = open("files_27_1/27A_2721.txt")
# n = int(f.readline())
# # n = 10
# m = [int(x) for x in f.readlines()]
# # m = [8, 30, 89, 91, 70, 88, 13, 32, 1, 12]
# c = 0
# for x, y in itertools.combinations(m, 2):
#     if x*y%65 == 0:
#         c+=1
# print(c)        #168
# B
# f = open("files_27_1/27B_2721.txt")
# n = int(f.readline())
# k65 = k = k5 = k13 = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 65 == 0:
#         k65 += 1
#     elif x % 13 == 0:
#         k13 += 1
#     elif x % 5 == 0:
#         k5 += 1
#     else:
#         k += 1
# print(k65*(k65-1)//2 + k65*(k+k5+k13) + k13*k5)

# 27890 A
# f = open("27-B_1.txt")
# n = int(f.readline())
# ms = 0
# mr5 = 10000000000
# for s in f:
#     n1, n2 = map(int, s.split())
#     ms += max(n1, n2)
#     if abs(n1-n2) % 5 != 0:
#         mr5 = min(mr5, abs(n1-n2))
#
# if ms % 5 != 0:
#     print(ms)
# else:
#     print(ms-mr5, "8")

# REGE https://inf-ege.sdamgia.ru/problem?id=29675
# f = open("inf_22_10_20_27b.txt")
# n = int(f.readline())
#
# m = [0]
# for s in f:
#     p = [int(x) for x in s.split()]
#     m = [a+b for a in p for b in m]
#     m = {x%3 : x for x in sorted(m)}.values()
#     # print(len(m))
# print(max(x for x in m if x%3 == 0))

# https://inf-ege.sdamgia.ru/problem?id=27990
# f = open("27990_B.txt")
# n = int(f.readline())
#
# m = [int(x) for x in f]
# k62 = k31 = k2 = k = 0
# for x in m:
#     if x % 62 == 0:
#         k62 += 1
#     elif x % 31 == 0:
#         k31 += 1
#     elif x % 2 == 0:
#         k2 += 1
#     else:
#         k += 1
# print(k31*k2 + k62*(k31+k2+k) + k62*(k62-1)/2)

# 1977 -(решать через индексы и сохранять длинну)
# f = open("27A_1977.txt")
# n = int(f.readline())
#
# m = [int(x) for x in f]
# k = [100000000]*43
# s = mx = 0
# for x in m:
#     s += x
#     if s % 43 == 0:
#         mx = max(mx, s)
#     mx = max(mx, s-k[s%43])
#     k[s%43] = min(k[s%43], s)
# print(mx, s)

# https://inf-ege.sdamgia.ru/problem?id=28129
# import itertools
# f = open("28129_A.txt")
# n = f.readline()
# # n = 4
# m = [int(x) for x in f]
# # m = [168, 7, 320, 328]
# isk = [-1]*2
# for x, y in itertools.combinations(m, r=2):
#     if (x%160 != y%160) and (x%7 == 0 or y%7 == 0):
#         if sum(isk) < x+y:
#             isk[0] = x
#             isk[1] = y
# print(isk)

# 7603
# f = open("27A_7603.txt")
# n = int(f.readline())
# k = int(f.readline())
# m = [int(x) for x in f]
# # n = 5
# # k = 3
# # m = [10, 15,100,1,30]
# lMax = maxSumm = 0
# for i in range(len(m)-k):
#     lMax = max(lMax, m[i])
#     maxSumm = max(maxSumm, lMax+m[i+k])
# print(maxSumm)

# 8513
# f = open("27_A_8513.txt")
# k = int(f.readline())       #кол-во минут
# n = int(f.readline())       #кол-во показаний
# m = [int(x) for x in f.readlines()]
# # k = 3
# # n = 5
# # m = [15, 10, 200, 0, 30]
# print(k,n,m)
# maxSumm = -100000
# for i in range(n):
#     for j in range(i+k, n):
#         maxSumm = max(maxSumm, m[i] + m[j])
# print(maxSumm)

f=open("27A.txt")
n = int(f.readline())       #кол-во чисел
k = int(f.readline())       #не более чем на
r = int(f.readline())       #не менее чем на
m = [int(x) for x in f.readlines()]
# n = 8
# k = 5
# r = 2
# m = [22, 36, 71, 55, 141, 82, 94, 177]
# print(n,k,r,m)
ans = []
for i in range(n):
    for j in range(i, n):
        if str(m[i]+m[j])[-2:] == "77":
            if r <= abs(i-j) <= k:
                ans.append([m[i], m[j]])
print(len(ans), ans[:100])








