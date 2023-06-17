"""for i in range(1, 20000):
    intI = i
    binI = bin(intI)[2::]
    binI = binI.replace("1", "A")
    binI = binI.replace("0", "1")
    binI = binI.replace("A", "0")
    intI = int(binI, 2)
    r = i - intI
    if r == 999:
        print(i, r)

#KEGE КИМ № 25014273
print(bin(20), int("100", 2))

#KEGE 422
for i in range(1, 1000):
    n = i
    base = 6
    r = ''
    while n > 0:
        d = str(n % base)
        r += str(d)
        n //= base
    r = r[::-1]
    r += r[-1]
    r = int(r, 6)
    r = bin(r)[2:]
    r += r[-1]
    r = int(r, 2)
    if r < 344:
        print(i, r)

#kege 563 23/11
for i in range(1,100):
    n = bin(i)[2::]
    n = n[::-1]
    n = int(n, 2)
    if n == 13:
        print(i, n)
"""
# 5358
# for i in range(6, 101):
#     n = bin(i)[2:]
#     summ = sum(int(x) for x in n[:3])
#     if summ % 2 == 0:
#         n = "1" + n[:-2] + "01"
#     else:
#         n = "10" + n[2:] + "1"
#     r = int(n,2)
#     if r > 50:
#         print(i)

# for i in range(1, 300):
#     count0 = bin(i)[2:].count("0")
#     n = bin(i-count0)[2:]
#     n = n[-3:] + n
#     if int(n, 2) > 224:
#         print(int(n, 2))

# 5660
# c=0
# for i in range(100, 201):
#     n = bin(i)[2::]
#     if len(n) % 2 == 0:
#         n += "10"
#     else:
#         n = "11" + n
#     r = int(n, 2)
#     if r % 2 == 0:
#         c += 1
# print(c)

# 5623
# for i in range(5, 2000):
#     n = bin(i)[2:]
#     if n.count("1") % 2 == 0:
#         n = '1'+n[:-2]+"10"
#     else:
#         n = "10"+n[2:]+"1"
#     if int(n, 2) > 202:
#         print(i)

# 5280
# for i in range(1, 300):
#     n = bin(i)[2:]
#     if n.count("1") % 2 == 0:
#         n = "1" + n[:-2] + "01"
#     else:
#         n = "1" + n[2:] + "10"
#     if int(n, 2) <= 100:
#         print(n, int(n, 2))

# 5694
# m = bin(278)[2:]
# for i in range(1, 200):
#     n = bin(i)[2:]
#     if len(m) > len(n):
#         n = (len(m)-len(n))*"0" + n
#     else:
#         m = (len(n)-len(m))*"0" + m
#     mass = []
#     for j in range(len(n)):
#         if n[j] == "1" or m[j] == "1":
#             mass.append("1")
#         else:
#             mass.append("0")
#     if mass[::-1].count("1") == 7:
#         print(i, n, m)
#         print("".join(mass[::-1]))

# 1
# c = []
# for i in range(1, 10000):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n = n + bin(n.count("1"))[2:]
#     else:
#         n = "1" + n + "00"
#     if int(n, 2) > 215:
#         c.append(i)
# print(min(c))

# 2
# m = []
# for i in range(1, 1000):
#     n = bin(i)[2:]
#     if n.count("1")%2 == 1:
#         n += "1"
#     else:
#         n += "0"
#     if n.count("1")%2 == 1:
#         n += "1"
#     else:
#         n += "0"
#     if int(n,2) < 80:
#         m.append(int(n,2))
# print(len(m), m)

# 3
# for i in range(1, 100000):
#     n = bin(i)[2:]
#     n = n.replace("1", "*").replace("0", "1").replace("*", "0")
#     if i-int(n,2) == 999:
#         print(i)

# 4
# for i in range(1, 10000):
#     n = bin(i)[2:]
#     if sum(int(x) for x in str(int(n, 2))) % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if sum(int(x) for x in str(int(n, 2))) % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if sum(int(x) for x in str(int(n, 2))) % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if int(n,2) > 1028:
#         print(int(n,2))

# for i in range(1, 1000):
#     n = bin(i)[2:]
#     if len(n) % 2 == 0:
#         n = n[:len(n)//2] + "111" + n[len(n)//2:]
#     else:
#         n = "11" + n[2:] + "1"
#     if int(n,2) > 4000:
#         print(n, int(n,2))

# c=0
# for i in range(10**7, 10**10):
#     n = bin(i)[2:]
#     if sum(int(x) for x in str(int(n, 2))) % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if sum(int(x) for x in str(int(n, 2))) % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if sum(int(x) for x in str(int(n, 2))) % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if 987654321 <= int(n,2) <= 2123456789:
#         c += 1
# print(c)

# 6588
# for i in range(1, 100):
#     n = bin(i)[2:]
#     n = "1" + n.replace("1", "*").replace("0", "1").replace("*", "0")
#     if n.count("1") % 2 == 0:
#         n += "0"
#     else:
#         n += "1"
#     if int(n,2) > 180:
#         print(i, int(n,2))

# 562
# n = "0"*(8-len(n)) + n
# n = f"{s:0>8}"
# for i in range(128, 255+1):
#     n = bin(i)[2:]
#     n = "0"*(8-len(n)) + n
#     n = n.replace("1", "*").replace("0", "1").replace("*", "0")
#     if i-int(n,2) == 105:
#         print(i, int(n,2))

# 5412
# c = 0
# for i in range(1, 92):
#     n = hex(i)[2:].upper()
#     if n.upper().count("B") % 2 == 0:
#         n = "1" + n
#     else:
#         n += "1"
#     if len(str(int(n,16))) == 2:
#         print(int(n,16), i)
#         c+=1
# print(c)

# 206
# import itertools
# c = 0
# for i in range(800, 901):
#     m = [''.join(x) for x in itertools.permutations(str(i), r=2) if x[0] != "0"]
#     massInt = []
#     for x in m:
#         massInt.append(int(x))
#     if max(massInt) - min(massInt) == 30:
#         print(i, max(massInt) - min(massInt))
#         c += 1
# print(c)

# 5694
# for i in range(1, 1000):
#     n = bin(i)[2:]
#     m = bin(278)[2:]
#     if len(n) > len(m):
#         m = "0" * (len(n)-len(m)) + m
#     else:
#         n = "0" * (len(m) - len(n)) + n
#     rez = ""
#     for j in range(len(m)):
#         if n[j] == "1" or m[j] == "1":
#             rez += "1"
#         else:
#             rez += "0"
#     if rez.count("1") == 7:
#         print(rez, i)

# 7607
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n = n + n[-3:]
#     else:
#         n = n + bin((i%3)*3)[2:]
#     if int(n,2) > 76:
#         print(i)

# 7584
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n += n[-3:]
#     else:
#         n += bin(3*(i%3))[2:]
#     if int(n,2) < 100:
#         print(i)

# 7807
# for i in range(1,80):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n += n[:2]
#     else:
#         n += bin(i%3)[2:]
#     if int(n,2) < 105:
#         print(int(n,2), i)

# for i in range(450000, 480000):
#     n = bin(i)[2:]
#     if i % 5 == 0:
#         n += bin(5)[2:]
#     else:
#         n += '1'
#     if int(n,2) % 7 == 0:
#         n += bin(7)[2:]
#     else:
#         n += '1'
#     if int(n,2) < 1855663:
#         print(int(n,2))

# for i in range(1, 40):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n += n[-3:]
#     else:
#         n += bin((i%3)*3)[2:]
#     if int(n,2) >= 76:
#         print(i)

# 8361
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if sum(int(x) for x in n) % 2 != 0:
#         n += "1"
#     else:
#         n += "0"
#     if sum(int(x) for x in n) % 2 != 0:
#         n += "1"
#     else:
#         n += "0"
#     if int(n, 2) < 100:
#         print(i, int(n, 2))

# 8493
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n += n[-3:]
#     else:
#         n += bin(i%3*3)[2:]
#     if int(n,2) < 76:
#         print(i)

# 8942
# for i in range(1,500):
#     n = bin(i)[2:]
#     if sum(int(x) for x in n) % 4 == 0:
#         n = "10" + n
#     else:
#         n = "11" + n
#     if sum(int(x) for x in n) % 2 == 0:
#         n += "1"
#     else:
#         n += "0"
#     if int(n,2) < 250:
#         print(i)

# for i in range(1,100):
#     s = bin(i)[2:]
#     if i % 5 == 0:
#         s += s[-3:]
#     else:
#         s = bin(i%5*5)[2:] + s
#     if int(s,2) > 512:
#         print(i)

# ans = []
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if str(i)[-1] == "8":
#         n = "100"+n[3:]
#     elif str(i)[-1] == "9":
#         n = n[:-3]+"110"
#     else:
#         c = 3 - len(bin(i%10)[2:])
#         n = n[:-3] + "0"*c + bin(i % 10)[2:]
#     if int(n,2) < 63:
#         ans.append([int(n,2), i])
#         print(i, int(n,2))

# for i in range(1,50):
#     n = bin(i)[2:]
#     if i % 5 == 0:
#         n += n[-3:]
#     else:
#         n += bin(i%5*5)[2:]
#     if int(n,2) > 256:
#         print(i)

# for i in range(1,1100):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n = "10" + n[2:] + "1"
#     else:
#         n = bin(i%3*2)[2:] + n
#     if int(n,2) > 8000:
#         print(i, int(n,2))

# 9360
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n += "010"
#     else:
#         n += bin(i%3*5)[2:]
#     if int(n,2) % 2 == 0 and int(n,2) > 300:
#         print(i)


# c = 0
# for i in range(1, 5000):
#     n = oct(i)[2:]
#     if i % 7 == 0:
#         n += n[-2:]
#     else:
#         n += oct(i%7*7)[2:]
#     if int(n,8) < 3000:
#         c += 1
# print(c)

# for i in range(1,460):
#     n = bin(i)[2:]
#     if n.count("0") % 2 == 0:
#         n += n[-2:]
#     else:
#         n = "1" + n + n[-1]
#     n += bin(i%2)[2:]
#     if int(n,2)  < 485:
#         print(i, int(n,2))




















