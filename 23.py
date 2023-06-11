"""#KEGE 4681
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if k > n:
        return f(n+3, k) + f(n*2, k)

print(f(3,27)*f(27,63))

#KEGE 633
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if k > n:
        return f(n+1,k) + f(n*2,k) + f(n**2, k)

print(f(5,154))

#KEGE 633+
def f(n,k):
    if n == k:
        return 1
    if n > k or n == 24:
        return 0
    if k > n:
        return f(n+1,k) + f(n*2,k) + f(n**2, k)

print(f(5,154))

#KEGE 1204
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if k > n:
        return f(n+1,k) + f(n*2,k)

print(f(2,7)*f(7,16)*f(16,39))

#3607
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if k > n:
        return f(n+2, k) + f(n*5, k)

print(f(2, 50))

#3627
def f(n, k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+2, k) + f(n*3,k)

print(f(1, 31))

#11358
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n<k:
        return f(n+1,k) + f(n+2,k) + f(n*2,k)

print(f(3,10)*f(10,12))

#3498
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+1, k) + f(n+3, k)
print(f(1,9)*f(9,17))

#13606
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+1,k)+f(n*2,k)+f(n*3,k)
print(f(2,14)*f(14,28))

#KEGE 633
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+1,k)+f(n*2,k)+f(n*n,k)
print(f(5,154))

#KEGE 104
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+1,k)+f(n*10,k)+f(n*2,k)+f(n*2+1, k)
print(f(1, 15))

#KEGE 933
def f(n,k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+3, k)+f(n*3,k)


couter = 0
for i in range(100):
    if i % 2 == 0:
        if f(3,i) >= 1:
            couter += 1
print(couter)

def f(n, k):
    if n == k:
        return 1
    if n == 3:
        return 0
    if n > k:
        return 0
    if n < k:
        return f(n+1,k) + f(n*2,k)
print(f(1,40))

#KEGE КИМ № 25014273
def f(n, k):
    if n == k:
        return 1
    if n > k:
        return 0
    if n < k:
        return f(n+2,k) + f(n*3,k) + f(n*4,k)

print(f(1,600))
"""


# 5138
# def f(n, k):
#     if n == k:
#         return 1
#     if n > k or n == 17:
#         return 0
#     if n < k:
#         return f(n+1, k) + f(n*2, k) + f(n**2, k)
#
# print(f(2, 16) * f(16, 65))

# 5676
# def f(n, k):
#     if n == k:
#         return 1
#     if n < k:
#         return 0
#     if n > k:
#         return f(n-3, k) + f(n//7, k)
#
# print(f(50, 1))

# 413
# def f(n, k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n+3,k) + f(n*2,k)
#
# print(f(1, 15))

# 633
# def f(n,k):
#     if n == k:
#         return 1
#     if n > k:
#         return 0
#     if n < k:
#         return f(n+1,k) + f(n*2,k) + f(n**2, k)
#
# print(f(5,154))

# 2344
# def f(n,k):
#     if n == k:
#         return 1
#     if n > k:
#         return 0
#     if n < k:
#         return f(n+1,k) + f(n+2,k) + f(n*4,k)
#
# print(f(1,13))

# 1301
# def f(n,k):
#     if n < k:
#         return 0
#     if n == k:
#         return 1
#     if n > k:
#         return f(n-2,k) + f(n-5,k)
#
# print(f(23, 2))

# 2345
# def f(n,k):
#     if n == k:
#         return 1
#     if n < k:
#         return 0
#     if n > k:
#         return f(n-1,k) + f(n-3,k) + f(n//3,k)
#
# print(f(22, 2))

# def f(n,k):
#     if n == k:
#         return 1
#     if n > k:
#         return 0
#     if n < k:
#         return f(n+2,k) + f(n + max(int(x) for x in str(n)), k)
#
# print(f(32, 55) * f(55, 76))

# def f(n, k, countMnoj):
#     if n == k and countMnoj == 1:
#         return 1
#     if n > k:
#         return 0
#     if n < k:
#         if countMnoj < 1:
#             return f(n + 1, k, countMnoj) + f(n + 2, k, countMnoj) + f(n * 2, k, countMnoj + 1) + f(n * 3, k,
#                                                                                                     countMnoj + 1)
#         else:
#             return f(n + 1, k, countMnoj) + f(n + 2, k, countMnoj)
#
# print(f(1, 11, 0))

# 6635
# import itertools
# m = [''.join(x) for x in itertools.product("12", repeat=13)]
#
# rez = []
# for alg in m:
#     s = 333
#     for com in alg:
#         if com == '1':
#             s -= 3
#         else:
#             s *= -3
#     if s < 0:
#         rez.append(s)
# print(len(rez), len(set(rez)))

# def f(n, k, plus, umn):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         if plus:
#             return f(n * 2, k, False, True) + f(n * 3, k, False, True)
#         if umn:
#             return f(n + 1, k, True, False) + f(n + 2, k, True, False)
#         if (plus == False) and (umn == False):
#             return f(n * 2, k, False, True) + f(n * 3, k, False, True) + f(n + 1, k, True, False) + f(n + 2, k, True,
#                                                                                                    False)
#
# print(f(1, 22, False, False))

# 20
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n*2,k)
# print(f(1,10)*f(10,20))

# 23
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n*2,k)
# print(f(1,12)*f(12,30))

# 65
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n+3,k) + f(n*2,k)
# print(f(3,9)*f(9,12)*f(12,20))

# 1376
# def f(n,k):
#     if n < k:
#         return 0
#     if n == k:
#         return 1
#     if n > k:
#         return f(n-8,k) + f(n//2,k)
# print(f(102,43)*f(43,5))

# 222
# def f(n,k):
#     if n == 6 or n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+2,k) + f(n*3,k)
# print(f(1, 25)*f(25,63))

# 951
# def f(n,k):
#     if n > k or n == 11 or n == 18:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n+2,k) + f(n*3,k)
# print(f(4,8)*f(8,23))

# 104
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) +  f(n*2,k) + f(n*2+1,k) + f(n*10,k)
# print(f(1, 15))

# 473
# def f(n,k):
#     if n > k or n == 43:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+2,k) + f(n+(n-1), k) + f(n+(n+1), k)
# print(f(7, 63))

# 1137
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n*2, k) + f(n*2+1, k)
# print(f(4, 29))

# 2342
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(pibav(n),k)
#
# def pibav(n):
#     result = ""
#     for x in str(n):
#         if x != "9":
#             result += str(int(x) + 1)
#         else:
#             result += x
#     return int(result)
#
# print(f(25,51))

# 2343
# def f(n,k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         if n % 2 == 0:
#             return f(n+1,k) + f(n*1.5,k)
#         else:
#             return f(n + 1, k)
# print(f(1,20))

# 2340 !!!
# from sys import setrecursionlimit
# setrecursionlimit(100000)
# def f(n, k):
#     if k == n:
#         return 1
#     if k < n:
#         return 0
#     if k > n:
#         return f(n + 2, k) + f(n + 4, k) + f(n + 5, k)
# for i in range(32, 100):
#     if f(31,i) == 1001:
#         print(i)

# 886
# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n,k,c):
#     if n > k:
#         return 0
#     if n == k and c != 7:
#         return 0
#     if n == k and c == 7:
#         return 1
#     if n < k:
#         return f(n+1, k, c+1) + f(n+4, k, c+1) + f(n*2, k, c+1)
# print(f(3,27,0))

# 2339
# def f(n,c):
#     if c == 15:
#         return 1
#     if c > 15:
#         return 0
#     if c < 15:
#         return f(n*2, c+1) + f(n*2+1,c+1)
# print(f(1,0))

# 2341 !!!
# d = set()
# def f(n, c):
#     if c == 8:
#         if 1000<=n<=1024:
#             d.add(n)
#     else:
#         f(n+1,c+1)
#         f(n+5,c+1)
#         f(n*3,c+1)
# f(1,0)
# print(d)

# 3030
# def f(n,k,mem):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         if mem < 1:
#             return f(n+1,k,mem) + f(n+2,k,mem) + f(n*2,k,mem+1)
#         if mem == 1:
#             return f(n+1,k,0) + f(n+2,k,0)
# print(f(1,15,0))

# 3162
# def f(n,k,mem):
#     if n > k:
#         return 0
#     if n == k and mem != 1:
#         return 0
#     if n == k and mem == 1:
#         return 1
#     if n < k:
#         if mem != 1:
#             return f(n+1,k,mem) + f(n+2,k,mem) +f(n*2,k,1)
#         if mem == 1:
#             return f(n + 1, k, mem) + f(n + 2, k, mem)
# print(f(2,12, 0))

# 4275
# def f(n,k,mem):
#     if n > k:
#         return 0
#     if n == k and mem <= 3:
#         return 1
#     if n == k and mem > 3:
#         return 0
#     if n < k:
#         if mem < 3:
#             return f(n+2,k,mem) + f(n*3,k,mem+1) + f(n*5,k,mem+1)
#         if mem >= 3:
#             return f(n+2,k,mem)
# print(f(2,200,0))

# 4492
# def f(n,k,mem):
#     if n % 2 != 0:
#         mem += 1
#     if n > k or mem > 1:
#         return 0
#     if n == k:
#         return mem == 1
#     if n < k:
#         return f(n+1,k,mem) + f(n+2,k,mem) + f(n*2,k,mem)
# print(f(2,40,0))

# 2714 -
# def f(n,k,mem):
#     if n % 2 == 0:
#         n += 1
#     if n > k or mem > 6:
#         return 0
#     if n == k and mem == 6:
#         return 1
#     if n == k and mem != 6:
#         return 0
#     if n < k:
#         return f(n+1,k,mem) + f(n+3,k,mem) + f(n+5,k,mem)
# print(f(3,25,0))

# 7623
# def f(n,k):
#     if n > k:
#         return 0
#     if n == 11:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n*2,k) + f(n*3,k)
# print(f(2,15)*f(15,25))

# 7599
# def f(n,k):
#     if n > k:
#         return 0
#     if n == 13:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n+2,k) + f(n*3,k)
#
# print(f(3,8)*f(8,18))

# 7823
# def f(n,k):
#     if n > k:
#         return 0
#     if n == 5:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n-1,k) + f(n//2,k) + f(n//3,k)
#
# print(f(26,11)*f(11,2))

# def f(n,k):
#     if n > k:
#         return 0
#     if n == 13 or n == 17:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n+3,k) + f(n*2,k)
#
# print(f(3,10) * f(10,22))

# def f(n,k):
#     if n > k:
#         return 0
#     if n == 15:
#         return 0
#     if n == k:
#         return 1
#     if n < k:
#         return f(n+1,k) + f(n*2, k) + f(n*3,k)
#
# print(f(1, 11) * f(11, 25))

# 8508
# def f(n, k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n == 12:
#         return 0
#     if n < k:
#         return f(n+1, k) + f(n+2,k) + f(n*2, k)
#
# print(f(2,9)*f(9,17))

# 8958
# def f(n, k):
#     if n < k:
#         return 0
#     if n == k:
#         return 1
#     if n == 22:
#         return 0
#     if n > k:
#         return f(n-2,k) + f(n//2,k) + f(n//3,k)
#
# print(f(40, 2))

# def f(n,k):
#     if n < k:
#         return 0
#     if n == k:
#         return 1
#     if n == 8:
#         return 0
#     if n > k:
#         return f(n-2,k) + f(n//2,k)
#
# print(f(70,22)*f(22,5))

# def f(n,k):
#     if n < k:
#         return 0
#     if n == k:
#         return 1
#     if n > k:
#         return f(n-sum(int(x) for x in str(n)), k) + f(n//2, k) + f(n-1, k)
# print(f(40, 25)*f(25,10))


def f(n,k):
    if n > k:
        return 0
    if n == 90:
        return 0
    if n == k:
        return 1
    if n < k:
        return f(n+1,k) + f(n*2,k) + f(n*3,k)

print(f(3, 30)*f(30,100)*f(100,184))




















