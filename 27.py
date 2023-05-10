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
f = open("inf_22_10_20_27b.txt")
n = int(f.readline())

m = [0]
for s in f:
    p = [int(x) for x in s.split()]
    m = [a+b for a in p for b in m]
    m = {x%3 : x for x in sorted(m)}.values()
    # print(len(m))
print(max(x for x in m if x%3 == 0))



























