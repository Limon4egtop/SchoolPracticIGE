""""#KEGE 16
def G(n):
    if n > 2:
        return F(n-1) - G(n-2)
    else:
        return n

def F(n):
    if n > 2:
        return G(n) + F(n-2)
    else:
        return n

print(G(15))

#KEGE 4736
def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)-1
print(f(1000)//f(997))

print(1000*(999*(998*1-1)-1)-1, 1000*998*997)    #997001999

#KEGE КИМ № 25014273
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2*n-1) * f(n-1)

print(f(3516)//f(3513))
"""
#4704
# from sys import *
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n-1)
# setrecursionlimit(10000)
# print(f(2023)/f(2020))

# 5671
# from sys import setrecursionlimit
# def f(n):
#     if n <= 10:
#         return n
#     if n >= 10000:
#         return 1
#     if n % 2 == 0:
#         return n%10 + f(n+2)
#     else:
#         return f(n-2) - (n-1) % 10
# setrecursionlimit(10000)
# print(f(4500) + f(5515))

# 5634
# from sys import setrecursionlimit
# setrecursionlimit(10000)
#
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) + n * f(n-1)
#
# print(f(5997)/f(5995))

# 5291
# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n < 3:
#         return 1
#     if n > 2:
#         if n % 2 != 0:
#             return f(n-1) + n
#         else:
#             return f(n - 3) + 2*n
#
# print(f(2048) - f(2041))

# def f(n):
#     if n <= 0:
#         return n
#     if 0 < n < 10000:
#         if n % 2 == 0:
#             return f(n//2) + n*5
#         else:
#             return f(n-4) - f(n-6)
#
# print(f(70) + f(56) - f(66) - f(44))


# from sys import setrecursionlimit
# setrecursionlimit(100000)
# def f(a,b):
#     if a == 0 and b == 0:
#         return 0
#     if a > b:
#         return f(a-1, b) + b
#     if a <= b and b > 0:
#         return f(a,b-1)+a
#
# c = 0
# for a in range(1, 10000):
#     if any(f(a,b) for b in range(1, 21) if f(a,b) == 2097152):
#         c+=1

# 6596
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) * (2*n - 3)
#
# print(f(516)/f(513))

# 7618
# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + f(n+2)
# print(f(2022)-f(2023))

# 7595
# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + 3 + f(n+3)
# print(f(23) - f(21))

# 7818
# def f (n):
#     if n >= 2073:
#         return n + 3
#     if n < 2073:
#         return n + f(n+2) - f(n+3)
#
# print(f(2070) + f(2069))

# def f(n):
#     if n > 1000000:
#         return n
#     else:
#         return n + f(2*n)
#
# def g(n):
#     return f(n)/n
#
# gg = g(2000)
# c = 0
# for i in range(1, 2001):
#     if gg == g(i):
#         c += 1
# print(c)

# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + f(n+2)
# print(f(2022) - f(2023))

# 8372
# print(int("100000100001000100101", 2))
# def f(n):
#     if n < 2:
#         return n
#     if n >= 2:
#         return f(n//2)*10 + n%2
# print(f(1065509))
# if f(1065509) == 100000100001000100101:
#     print(True)

# 8520
# def f(n):
#     if n >= 2025:
#         return n
#     else:
#         return n + 3 + f(n+3)
# print(f(2018)-f(2022))


# 8953
# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n >=10000:
#         return 1
#     else:
#         if n % 2 == 0:
#             return f(n+3) + 7
#         else:
#             return f(n+1)-3
# print(f(50)-f(57))

# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n >= 2222:
#         return 1
#     else:
#         return n**3 + f(n+2)
# print(f(4)-f(10))

# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n >= 9026:
#         return 2*n
#     if n % 2 == 0:
#         return f(n+3) + 2*n
#     else:
#         return f(n+2) + 2*n - 1
# print(f(9019) - f(9022))

# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n < 3:
#         return 2
#     if n > 2:
#         return 2*f(n-2)
# print(f(2222)/f(2182))






































