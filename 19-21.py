# REGE 27820   https://inf-ege.sdamgia.ru/problem?id=27820
# def f(s, c, m):
#     """
#
#     :param s: после какого числа победа
#     :param c: текущий ход
#     :param m: хочу чтобы победил
#     :return:
#     """
#     if s >= 42:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#
#     h = [f(s+1, c+1, m), f(s+2, c+1, m), f(s*2, c+1, m)]
#     return any(h) if (c+1) % 2 == m % 2 else all(h)         #all - все ходы(умный); any - любой ход(дурак)
#
# for s in range(1, 42):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 4 or m == 2:
#                 print(s, m)


# https://inf-ege.sdamgia.ru/problem?id=27416
# https://inf-ege.sdamgia.ru/problem?id=27417
# https://inf-ege.sdamgia.ru/problem?id=27418
"""def f(a,b,c,m):
    if a + b >= 77:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(a+1, b, c+1, m), f(a, b+1, c+1, m), f(a*2, b, c+1, m), f(a, b*2, c+1, m)]
    return any(h) if (c+1) % 2 == m % 2 else any(h)        #27416
    return any(h) if (c+1) % 2 == m % 2 else all(h)       #27417

for s in range(1, 70):
    for m in range(1,5):
        if f(7, s, 0, m):
            #if m == 2:                     #27416
            if m == 2 or m == 4:            #27417
                print(s, m)

#KEGE 840
#(2 кучи) +1 *4 >=133       1<=S<=125
def f(a,b,c,m):
    if a + b >= 133:
        return c%2 == m%2
    if c == m:
        return 0
    h = [f(a+1, b, c+1, m), f(a*4, b, c+1, m), f(a, b+1, c+1, m), f(a, b*4, c+1, m)]
    return any(h) if (c+1) % 2 == m%2 else all(h)

for s in range(1, 125+1):
    for m in range(1,5):
        if f(7, s, 0, m):
            if m == 2 or m == 4:
                print(s, m)       #19 - 8; 20 - 2031; 21 - 30
"""


# 4379
# def f(s, c, m):
#     if s>=51:
#         return c%2 == m%2
#     if c == m:
#         return False
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m)]
#     if s*2 <= 60:
#         h.append(f(s*2, c+1, m))
#     return any(h) if ((c+1) % 2) == (m % 2) else all(h)
#
# for s in range(1,50+1):
#     #for m in range(1, 5):      #19
#     for m in range(1, 7):       #20
#         if f(s,0,m):
#             if m == 1 or m == 3:
#                 print(s, m)

# 4679
# def f(s, c, m):
#     if s >= 165:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#
#     h = [f(s+1, c+1, m), f(s+4, c+1, m), f(s*2, c+1, m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 164):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 4599
# def f(a,b,c,m):
#     if a + b >= 259:
#         return c % 2 == m % 2
#     if c > m:
#         return 0
#
#     h = [f(a+1, b, c + 1, m), f(a, b+1, c + 1, m),
#          f(a*2, b, c + 1, m), f(a, b*2, c + 1, m)]
#     return any(h) if (c+1) % 2 == m % 2 else all(h)
#
# for s in range(1, 242):
#     for m in range(1, 5):
#         if f(17, s, 0, m):
#             if m == 3 or m == 1:
#                 print(s, m)

# 5674
# def f(s, c, m):
#     if s > 29:
#         return c % 2 == m % 2
#     if c > m:
#         return 0
#     h = [f(s+6,c+1,m)]
#     if s % 2 == 0:
#         h.append(f(s+4,c+1,m))
#     else:
#         h.append(f(s+s%10,c+1,m))
#
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(2, 26):
#     for m in range(1, 5+1):
#         if f(s, 0, m):
#             if m == 5 or m == 3 or m == 1:
#                 print(s, m)

# 847
# def f(s, c, m):
#     if s > 33:
#         return c % 2 == m % 2
#     if c == m:
#         return False
#     h = [f(s+1, c+1, m), f(s+2, c+1, m), f(s+3, c+1, m), f(s*2, c+1, m)]
#     return any(h) if (c+1) % 2 == m % 2 else all(h)
#
# for s in range(1, 33):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)


# 845
# def f(s, c, m):
#     if s >= 36 and s <= 60:
#         return c % 2 == m % 2
#     if s > 60:
#         return (c-1) % 2 == m % 2
#     if c == m:
#         return 0
#     h = [f(s + 1, c + 1, m)]
#     h.append(f(s * 2, c + 1, m))
#     h.append(f(s * 3, c + 1, m))
#
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 36):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2:
#                 print(s, m)

# 1202
# def f(a, b, c ,m):
#     if a+b >= 59:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,b,c+1,m), f(a*2,b,c+1,m), f(a,b+1,c+1,m), f(a,b*2,c+1,m)]
#     return any(h) if (c+1)% 2 == m%2 else all(h)
#
# for s in range(1, 200):
#     for m in range(1, 5):
#         if f(5, s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 853 +1 *2 2кучи >=77 1<=S<=69 a=7
# def f(a,b,c,m):
#     if a+b >= 77:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,b,c+1,m), f(a*2,b,c+1,m), f(a,b+1,c+1,m), f(a,b*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 100):
#     for m in range(1, 5):
#         if f(7, s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 1135 2кучи +1 +другаяКуча a+b>=68 a=8 1<=S<=59
# def f(a,b,c,m):
#     if a+b >= 68:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,b,c+1,m), f(a+b,b,c+1,m), f(a,b+1,c+1,m), f(a,b+a,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 100):
#     for m in range(1, 5):
#         if f(8, s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 1420 2кучи +1 *2 a*b>=63 a=2 1<=s<=31
# def f(a,b,c,m):
#     if a*b >= 63:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,b,c+1,m), f(a*2,b,c+1,m), f(a,b+1,c+1,m), f(a,b*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 100):
#     for m in range(1, 5):
#         if f(2, s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 2369 3кучи +3 +13 +23 a+b+x>=73 a=2 b=s x=2s 1<=s<=23
# def f(a,b,x,c,m):
#     if a+b+x >= 73:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+3,b,x,c+1,m), f(a+13,b,x,c+1,m), f(a+23,b,x,c+1,m),
#          f(a,b+3,x,c+1,m), f(a,b+13,x,c+1,m), f(a,b+23,x,c+1,m),
#          f(a,b,x+3,c+1,m), f(a,b,x+13,c+1,m), f(a,b,x+23,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 23):
#     for m in range(1, 5):
#         if f(2, s, s*2, 0, m):
#             if m == 2:
#                 print(s, m)

# https://kpolyakov.spb.ru 1 куча +2 *2 1<=s<=24 >=25
# def f(s, c, m):
#     if s >= 25:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+2,c+1, m), f(s*2,c+1, m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 25):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 1 or m == 3:
#                 print(s, m)

# kpolyakov.spb.ru 40 1 куча +3 *2 >=33 1<=S<=32
# def f (s,c,m):
#     if s >= 33:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+3,c+1,m), f(s*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 32):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# kpolyakov.spb.ru 41 1 куча +2 *3 >=50 1<=s<=49
# def f(s,c,m):
#     if s >= 50:
#         return c%2==m%2
#     if c == m:
#         return 0
#     h = [f(s+2,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 49):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# kpolyakov.spb.ru 42 1 куча +2 +3 *2 >=30 1<=s<=29
# def f(s, c, m):
#     if s >= 30:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#     h = [f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 29):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# kpolyakov.spb.ru 43 1 куча +1 +2 +3 *2 >=34 1<=s<=33
# def f(s,c,m):
#     if s >= 34:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s+2,c+1,m), f(s+3,c+1,m), f(s*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 33+1):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# kpolyakov.spb.ru 47 1 куча +1 *2 *3 >=36 1<=s<=35
# def f (s,c,m):
#     if s >= 36 and s <= 60:
#         return c%2 == m%2
#     if s > 60:
#         return c%2 != m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s*2,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 36):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2:
#                 print(s,m)

# kpolyakov.spb.ru 48 1 куча +1 *2 *3 (>=43 and <=72) 1<=s<=42
# def f (s, c, m):
#     if s > 72:
#         return c%2 != m%2
#     if s >= 43 and s <= 72:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s*2,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s,m)

# kpolyakov.spb.ru 80 +1 *2 (>=25 and <=45)  1 <= s <= 24
# def f(s,c,m):
#     if s > 45:
#         return c%2 != m%2
#     if s >= 25 and s <= 45:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 25):
#     for m in range(1,5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# 5136
# def f(s, c, m):
#     if s <= 12:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#     if s % 2 == 0:
#         h = [f(s - 1, c + 1, m), f(s // 2, c + 1, m)]
#     else:
#         h = [f(s - 1, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(13, 150):
#     for m in range(5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 4476 2 кучи +2 *2 >=231 a=17 1<=s<=213
# def f (a,b,c,m):
#     if a+b >= 231:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+2,b,c+1,m), f(a*2,b,c+1,m), f(a,b+2,c+1,m), f(a,b*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 213):
#     for m in range(1, 5):
#         if f(17, s, 0, m):
#             if m == 2 or m == 4:
#                 print(s,m)

# 1349 - /2 /(*2/3) (if s%2==0 or s%3 == 0) (if s%2 != 0: s-2) (if s%3 != 0: s-3) 2<=s<=37 <= 1
# def f(s,c,m):
#     if s <= 1:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = []
#     if s % 2 != 0:
#         h.append(f(s-2, c+1, m))
#     if s % 3 != 0:
#         h.append(f(s-3, c+1, m))
#     if s % 2 == 0 and s % 3 == 0:
#         h.append(f(s//2, c+1, m), f(s - s*2//3, c+1, m))
#     return any(h) if (c + 1) % 2 == m % 2 else any(h)
#
# for s in range(2, 38):
#     for m in range(6):
#         if f(s, 0, m):
#             if m == 1 or m == 3:
#                 print(s, m)

# 1 куча +1 +2 (*3 if i%3 == 0)  >= 56 1<=s<=55 -
# def f(s, c, m):
#     if s >= 56:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m)]
#     if s % 3 == 0:
#         h.append(f(s * 3, c + 1, m))
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)


# for s in range(1, 56):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 3 or m == 1:
#                 print(s, m)

# 6608 1 куча //3(округлить до меньшего) -12 <= 12 S>=13
# def f(s,c,m):
#     if s <= 12:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s//3,c+1,m), f(s-12,c+1,m)]
#     return any(h) if (c+1) % 2 == m%2 else all(h)
#
# for s in range(13, 100):
#     for m in range(1,5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

#Task of course - Одна куча (19-21) - 29/03/23
# def f(x, c, m):
#     if x >= 55:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#     h = [f(x + 2, c + 1, m), f(x * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1,50):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 2:
#                 print(s, m)

# 7621 1 куча +1 +4 *3 >=43 1<=s<=42
# def f(s,c,m):
#     if s >= 43:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s+4,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# 7598 1 куча +1 +4 *4 >= 78 1<=s<=77
# def f(s,c,m):
#     if s >= 78:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1, c+1, m), f(s+4, c+1, m), f(s*4, c+1, m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 78):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 7821 1 куча +1 +3 *5 >=420 1<=s<=419
# def f(s,c,m):
#     if s >= 420:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s+3,c+1,m), f(s*5,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 420):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 2 кучи (в большую или = +1 +2 +3) (в меньшую *2) >= 48
# def f(a,b,c,m):
#     if a >= 48 or b >= 48:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = []
#     if a >= b:
#         h = [f(a+1,b,c+1,m), f(a+2,b,c+1,m), f(a+3,b,c+1,m), f(a,b*2,c+1,m)]
#     else:
#         h = [f(a,b+1,c+1,m), f(a,b+2,c+1,m), f(a,b+3,c+1,m), f(a*2,b,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for b in range(1, 48):
#     for m in range(1,5):
#         if f(39,b,0,m):
#             if m == 2 or m == 4:
#                 print(b,m)

# 1 куча +1 +4 *3 >=43 1<=s<=42
# def f(s,c,m):
#     if s >= 43:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s+4,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 8506 1 куча +1 +4 *3 >= 55 1<=s<=54
# def f(s,c,m):
#     if s >= 55:
#         return c%2 == m%2
#     if m == c:
#         return 0
#     h = [f(s+1,c+1,m), f(s+4,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 55):
#     for m in range(1,5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 2 кучи +1 +3 *2 >=159 a=7 1<=s<=130
# def f(a,s,c,m):
#     if a+s >= 159:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,s,c+1,m), f(a+3,s,c+1,m), f(a*2,s,c+1,m), f(a,s+1,c+1,m), f(a,s+3,c+1,m), f(a,s*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 131):
#     for m in range(1,5):
#         if f(7,s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# 1 куча +1 +4 *3 >=73 1<=s<=72
# def f(s,c,m):
#     if s >=73:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s+1,c+1,m), f(s+4,c+1,m), f(s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 73):
#     for m in range(1, 5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s, m)

# 2 кучи +1 *2 a*s>=455 a=5 1<=s<=90
# def f(a,s,c,m):
#     if a*s >= 455:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,s,c+1,m), f(a*2,s,c+1,m), f(a,s+1,c+1,m), f(a,s*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 91):
#     for m in range(1,5):
#         if f(5, s, 0, m):
#             if m == 2 or m == 4:
#                 print(s, m)


# def f(s,c,m):
#     if s <= 32:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s-3,c+1,m), f(s-2,c+1,m)]
#     if s % 4 == 0:
#         h.append(f(s//4,c+1,m))
#     return any(h) if (c+1)%2==m%2 else all(h)
#
# for s in range(32, 1000):
#     for m in range(1,5):
#         if f(s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# 9374 2 кучи a=3 1<=s<=40 +2 *2 a*b>=123
# def f(a,s,c,m):
#     if a*s >= 123:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+2,s,c+1,m), f(a*2,s,c+1,m), f(a,s+2,c+1,m), f(a,s*2,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 41):
#     for m in range(1,5):
#         if f(3,s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

# 2 кучи +1 *3 a+s>=175 a=19 1<=s<=154
# def f(a,s,c,m):
#     if a+s >= 175:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(a+1,s,c+1,m), f(a*3,s,c+1,m), f(a,s+1,c+1,m), f(a,s*3,c+1,m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s in range(1, 155):
#     for m in range(1,5):
#         if f(19,s,0,m):
#             if m == 2 or m == 4:
#                 print(s,m)

































