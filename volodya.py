# def f(n, k, mem):
#     if n == k and mem == 1:
#         return 1
#     if n > k:
#         return 0
#     if mem == 1:
#         return f(n+1, k, 1) + f(n+2, k, 1)
#     else:
#         return f(n+1, k, 0) + f(n+2, k, 0) + f(n*2, k, 1) + f(n*3, k, 1)
#
# print(f(1, 11, 0))

# 25 | 6210
# import fnmatch
# counter = 0
# for i in range(212, 10**7+1, 53):
#     if fnmatch.fnmatch(str(i), "*2?2*"):
#         # Палиндром
#         if str(i) == str(i)[::-1]:
#             # Сумма цифр
#             if sum(int(x) for x in str(i)) > 10:
#                 # Проверка на простые числа
#                 if all(i % x != 0 for x in range(2, i)):
#                     # Массив делителей
#                     m = [x for x in range(1, i+1) if i % x == 0]
#                     # Кол-во делителей
#                     if len(m) > 30:
#                         print(i, sum(m))

# def f(x, a1, a2):
#     return ((80 <= x <= 16) or (250 <= x <= 40)) <= (a1 <= a2)
#
# r = []
# for a1 in range(6, 50):
#     for a2 in range(6, 51):
#         if all(f(x, a1, a2) for x in range(1, 100)):
#             r.append(a2 - a1)
#
# print(min(r))

# 15 | 199, 435
# def f(x, a1, a2):
#     return ((22 <= x <= 35) <= (a1 <= x <= a2)) and (not(15 <= x <= 30) or (a1 <= x <= a2))
#
#
# r = []
# for a1 in range(10, 40):
#     for a2 in range(10, 41):
#         if all(f(x, a1, a2) for x in range(1, 100)):
#             r.append(a2 - a1)
#
# print(min(r))

# Более точный вариант
# def f(x, a1, a2):
#     return ((220 <= x <= 350) <= (a1 <= x <= a2)) and (not(150 <= x <= 300) or (a1 <= x <= a2))
#
#
# r = []
# for a1 in range(100, 400):
#     for a2 in range(100, 410):
#         if all(f(x, a1, a2) for x in range(1, 1000)):
#             r.append(a2 - a1)
#
# print(min(r) // 10)

# 435
# def f(x, a1, a2):
#     return not((a1 <= x <= a2) and not((120 <= x <= 460) or (200 <= x <= 300)))
#
#
# r = []
# for a1 in range(100, 470):
#     for a2 in range(100, 470):
#         if all(f(x, a1, a2) for x in range(1, 1000)):
#             r.append(a2 - a1)
#
# print(max(r) // 10)

# Решу ЕГЭ - 45260 дома

# 17 | 3749

# import math
#
# m = [int(x) for x in open('17_3749.txt').readlines()]
#
# max_q = 0
# for x in m:
#     if math.sqrt(x).is_integer():
#         max_q = max(max_q, x)
#
# c = 0
# max_el = 0
# min_el = 10 ** 10 + 1
#
# for i in range(len(m) - 1):
#     sr_g = math.sqrt(m[i] * m[i + 1])
#     if sr_g == int(sr_g) and (m[i] <= max_q * 3 or m[i + 1] <= max_q * 3):
#         c += 1
#         max_el = max(max_el, sr_g)
#         min_el = min(min_el, sr_g)
#
# print(c, max_el, min_el)


# komp ege 17 | 3370
# m = [int(x) for x in open('17_3370.txt').readlines()]
#
# sum_f = sum(int(str(abs(x))[0]) for x in m)
#
# c = 0
# ms = 0
#
# for i in range(len(m) - 1):
#     if m[i] * m[i+1] > sum_f:
#         c += 1
#         ms = max(ms, m[i] + m[i + 1])
#
# print(c, ms)

# 15 | 344
# for A in range(0, 100):
#     c = 1
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if not((5*x + 3*y != 60) or ((A > x) * (A > y))):
#                 c *= 0
#     if c == 1:
#         print(A)
# 21

# 15 | 345
# for A in range(0, 100):
#     c = 1
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if not((2*x + 3*y != 72) or ((A > x) * (A > y))):
#                 c *= 0
#     if c == 1:
#         print(A)
# 37

# 15 | 122
# for A in range(1, 1000):
#     c = 1
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             # if not((x % A != 0 and (x % 15 != 0)) <= ( x % 18 != 0 or (x % 15 != 0 ) )):
#             if not(((x % A != 0) and (x % 15 == 0)) <= ((x % 18 != 0) or (x % 15 != 0))):
#                 c *= 0
#     if c == 1:
#         print(A)
# 90

# 25 | 3025
# def d(n):
#     r = []
#     d = 2
#     while d * d < n:
#         if n % d == 0:
#             r.append(d)
#             r.append(n // d)
#         d += 1
#
#     if d * d == n:
#         r.append(d)
#
#     r.sort()
#
#     return r
#
#
# for n in range(200000000, 2000000000):
#     m = [x for x in d(n) if x % 2 != 0]
#
#     if len(m) > 5:
#         print(n, m[-6])

# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443

# 25 | 2943
# def d(n):
#     r = []
#     d = 2
#     while d * d < n:
#         if n % d == 0:
#             r.append(d)
#             r.append(n // d)
#         d += 1
#
#     if d * d == n:
#         r.append(d)
#
#     r.sort()
#
#     return r
#
# for x in range(220000, 2000000):
#     c = d(x)
#     if len(c) > 1:
#         m = c[0] + c[-1]
#
#         if str(m)[-1] == '4':
#             print(x, m)
# 220004 110004
# 220023 73344
# 220024 110014
# 220033 20014
# 220043 1044
#

# 25 | 5985
# import fnmatch
#
# def d(n):
#     r = []
#     d = 2
#     while d * d < n:
#         if n % d == 0:
#             r.append(d)
#             r.append(n // d)
#         d += 1
#     if d * d == n:
#         r.append(d)
#     r.sort()
#     return r
#
#
# for x in range(1, 10 ** 7 + 1):
#     n = fnmatch.fnmatch(str(x), "12*348")
#     if n and x % 12 == 0:
#         r = d(x)
#         if len(r)+2 == 12:
#             print(x, r[-1])

# 126348 63174
# 1203348 601674
# 1215348 607674
# 1242348 621174
# 1257348 628674
# 1266348 633174
# 1275348 637674
# 1287348 643674

# 25 | 5912
# import fnmatch
#
# def d(n):
#     r = []
#     d = 2
#     while d * d < n:
#         if n % d == 0:
#             r.append(d)
#             r.append(n // d)
#         d += 1
#
#     if d * d == n:
#         r.append(d)
#
#     r.sort()
#
#     return r
#
#
# for x in range(1, 10 ** 7 + 1):
#     n = fnmatch.fnmatch(str(x), "12?*45")
#     if n:
#         r = d(x)
#         if len(r) == 18:
#             print(x, r[-1])

# 1202445 400815
# 1234845 411615
# 1251045 417015
# 1259145 419715
# 1283445 427815
# 1299645 433215