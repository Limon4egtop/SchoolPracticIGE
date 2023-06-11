"""#KEGE 75
print("z x y")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = (not x and y and z) or (not x and not y and z) or (not x and not y and not z)
            if F == 1:
                print(z,x,y)

#https://kompege.ru/variant?kim=25005700
print("h l w n")
for h in 0,1:
    for l in 0,1:
        for w in 0,1:
            for n in 0,1:
                F = (not(h <= l)) <= ((not(w <= n)) and h)
                if F == 0:
                    print(h, l, w, n)

#статград
print("w x y z")
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                F = (x <= (y == w)) and (y == (w <= z))
                print(w,x,y,z,F.real)

#KEGE КИМ № 25014273
print("w x y z")
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                F = ((x and not(y)) == (z or not(w)) <= (x and z))
                if F == 0:
                    print(w, x, y, z)

print("x z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((z<=x) and (x <= w)) or (y == (z or x))
                if f == 0:
                    print(x,z,w)

print("x y w z")
for x in 0,1:
    for y in 0,1:
        for w in 0, 1:
            for z in 0, 1:
                if (((x <= y) and (y <= w)) or (z == (x or y))) == 0:
                    print(x, y, w, z)

print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((y <= z) or (not (x) and w)) == (w == z)
                if f == 1:
                    print(x,y,z,w)

#70
print("X W Y Z")
for x in 0,1:
    for w in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (x or not(y)) and not(y == z) and w
                if f == 1:
                    print(x, w, y, z)

#74
print("a b c")
for a in 0,1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a and not(c)) or (not(b) and not(c))
            print(a, b, c, f)

#75
print("x y z")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not(y) and not(z))
            if f == 1:
                print(x, y, z)

#76
print("x y z w")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not(x) and y) == z) and w
                if f == 1:
                    print(x, y, z, w)

#78
print("y w x z")
for x in 0,1:
    for w in 0, 1:
        for z in 0, 1:
            for y in 0, 1:
                f = (x <= (y and not(z))) or w
                if f == 0:
                    print(y, w, x, z)

#83
print("w x y z")
for z in 0,1:
    for y in 0, 1:
        for x in 0, 1:
            for w in 0, 1:
                f = (x and not(y)) or (x == z) or w
                if f == 0:
                    print(w,x,y,z)

#734
print("x y z")
for z in 0,1:
    for y in 0, 1:
        for x in 0, 1:
            f = (not(x) and y and z) or (not(x) and not(z))
            if f == 1:
                print(x,y,z)

#735
print("x y z w")
for x in 0,1:
    for w in 0, 1:
        for z in 0, 1:
            for y in 0, 1:
                f = not(y) and x and (not(z) or w)
                if f == 1:
                    print(x,y,z,w)

#791
print("x y z w")
for w in 0,1:
    for z in 0, 1:
        for y in 0, 1:
            for x in 0, 1:
                f = (y <= (x or z)) and (z <= y)
                if f == 0:
                    print(x,y,z,w)

#816
print("x y z f")
for y in 0,1:
    for x in 0, 1:
        for z in 0, 1:
            f = not(x == (y <= z))
            print(x,y,z,f)

#1185
print("w x y z")
for x in 0,1:
    for w in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (y <= x) or not((x <= z) and (z <= x)) and not(w)
                if f == 0:
                    print(w,x,y,z)

#79
print("w y z x")
for z in 0,1:
    for x in 0, 1:
        for w in 0, 1:
            for y in 0, 1:
                f = not(w) and ((y or z) <= (not(x) and y))
                if f == 1:
                    print(w,y,z,x)

#1267
print("w x y z")
for x in 0,1:
    for z in 0, 1:
        for w in 0, 1:
            for y in 0, 1:
                f = ((w <= y) or not(y <= z)) and not(x) and not(x == z)
                if f == 1:
                    print(w,x,y,z)

#1282
print("w z x y")
for w in 0,1:
    for z in 0, 1:
        for y in 0, 1:
            for x in 0, 1:
                f = (x <= y) or not(w <= z)
                if f == 0:
                    print(w,z,x,y)

#1357
print("a b c d")
for a in 0,1:
    for d in 0, 1:
        for c in 0, 1:
            for b in 0, 1:
                f = ((a and b) == (not(c))) and (b <= d)
                if f == 1:
                    print(a,b,c,d)

#1422
print("w x z y")
for w in 0,1:
    for z in 0, 1:
        for y in 0, 1:
            for x in 0, 1:
                f = not(z and (not(w))) or ((z <= w) == (x <= y))
                if f == 0:
                    print(w,x,z,y)

#1846
print("a b c d")
for d in 0,1:
    for c in 0, 1:
        for b in 0, 1:
            for a in 0, 1:
                 f = ((not(a)) and (not(b))) or (b == c) or d
                 if f == 0:
                     print(a,b,c,d)

#71
print("x z y w")
for w in 0,1:
    for z in 0, 1:
        for y in 0, 1:
            for x in 0, 1:
                f = ((z <= x) and (x <= w)) or (y == (z or x))
                if f == 0:
                    print(x,z,y,w)

#46
print("x y w z")
for w in 0,1:
    for z in 0, 1:
        for y in 0, 1:
            for x in 0, 1:
                f = (x and z) or ((w <= x) == (z <= y))
                if f == 0:
                    print(x,y,w,z)
"""
#85
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (x == (not(z))) <= ((x or w) == y)
#                 if f == 0:
#                     print(x,y,w,z)

# 5657
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = w and ((x <= y) == (y <= z))
#                 if f == 1:
#                     print(x,y,w,z)

# 5620
# print("w x y z")
# for x in 0,1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (not(z <= x)) or (y == w) or w
#                 if f == 0:
#                     print(w,x,y,z)

# 5277
# print("x y w z")
# for x in 0,1:
#     for y  in 0, 1:
#         for z  in 0, 1:
#             for w in 0, 1:
#                 f = not(w == y) and (z <= w) and (not(x))
#                 if f == 1:
#                     print(x,y,w,z)

# print("x y w z")
# for x in 0,1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = ((x <= z) and y) <= w
#                 if f == 0:
#                     print(x,y,w,z)

# print("x y w z")
# for x in 0,1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = ((x <= y) or (z <= w)) and ((z == y) <= (w == x))
#                 if f == 0:
#                     print(x,y,w,z)

# 6598
# print("x y w z")
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= w) and ((not(y)) <= z)) <= ((z == x) or (w and (not(y))))
#                 if f == 0:
#                     print(x,y,w,z)

# print("x y w z")
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f1 = (x or (not(y))) == (z <= w)
#                 f2 = ((not(x)) == y) and (z <= w)
#                 if f1 == 0 and f2 == 1 and y == 1 and z == 0:
#                     print(x, y, w, z, str(f1)[0], str(f2)[0])
#                     print("x y w z")
#                 if f2 == 0 and y == 1 and (x+y+w+z >= 2):
#                     print(x,y,w,z,str(f1)[0],str(f2)[0])

# 7604
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = not(y and (not(x))) and (not(x == z) and w)
#                 if f:
#                     print(x,y,w,z)

# 82
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 g = (x and (not(y))) or (y == z) or (not(w))
#                 if g == 0:
#                     print(x,y,w,z)

# 7604
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (not(y <= z)) or ((not(x)) <= (not(w))) or x
#                 if f == 0:
#                     print(x,y,w,z)

# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f1 = (x or (not(y))) <= (w == z)
#                 f2 = (x or (not(y))) == (z <= w)
#                 print(x,y,w,z,int(f1), int(f2))

# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (x or (not(y))) and (not(y == z)) and (not(w))
#                 if f:
#                     print(x,y,w,z)

# 8358
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (x or y or z) <= (x and (y or w))
#                 if f == 0 and x+y+w+z <= 2 and z == 0:
#                     print(x,y,w,z)

# 8489
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = ((w <= y) <= (x == y)) or (not(z))
#                 if f == 0:
#                     print(x,y,w,z)

# 8938
# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = ((x or y) == (y <= z)) or w
#                 if f == 0:
#                     print(x,y,w,z)

# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = (x <= y) or (not(w <= z))
#                 if f == 0:
#                     print(x,y,w,z)

# print("x y w z")
# for z in 0,1:
#     for w in 0,1:
#         for y in 0,1:
#             for x in 0,1:
#                 f = (not(x) or (y<=(not(z)))) and y and ((not(x)) == w)
#                 if f:
#                     print(x,y,w,z)

# print("x y w z")
# for z in 0,1:
#     for w in 0, 1:
#         for y in 0, 1:
#             for x in 0, 1:
#                 f = x and (not(y)) and (not(z) or w)
#                 if f:
#                     print(x,y,w,z)

print("x y w z")


































