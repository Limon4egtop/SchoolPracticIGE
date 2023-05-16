"""s = "111"
while "333" in s or "111" in s:
    if "333" in s:
        s.replace("3", "111", 1)
    else:
        s.replace("1", "333", 1)
print(len(s), s)

for i in range(1,100):
    string = "0"+"1"*i+"2"*i+"0"
    while not "00" in string:
        string = string.replace("011", "20", 1)
        string = string.replace("022", "10", 1)
        string = string.replace("01", "220", 1)
        string = string.replace("02", "110", 1)
    if string.count("1") == 47 and string.count("2") >= 70:
        print(i)

#KEGE 645 16.11
s = "1" * 46 + "2" * 31
while "1111" in s:
    s = s.replace("1111", "2", 1)
    s = s.replace("222", "1", 1)
print(s)

#No number 16.11
for x in range(1,100):
    for y in range(1,100):
        s = "1" * x + "2" * y
        while "1111" in s:
            s = s.replace("1111", "2", 1)
            s = s.replace("222", "1", 1)
        if s == "12":
            print(x, y)
            if x == 46 and y == 31:
                print("\n\n")

#KEGE 1119 16.11
for i in range(1, 100):
    for j in range(1, 100):
        for g in range(1, 100):
            s = "0"+"1"*i+"2"*j+"3"*g
            while ("01" in s) or ("02" in s) or ("03" in s):
                s = s.replace("01", "30", 1)
                s = s.replace("02", "3103", 1)
                s = s.replace("03", "1201", 1)
            if (s.count("1") == 31) and (s.count("2") == 24) and (s.count("3") == 46):
                print(g)

#KEGE 1115 16.11
for i in range(81, 200):
    n = bin(i)[2::]
    count0 = n.count("0")
    count1 = n.count("1")
    if count1 == count0:
        n += n[-1]
    if count1 > count0:
        n += "0"
    else:
       n += "1"

    count0 = n.count("0")
    count1 = n.count("1")
    if count1 == count0:
        n += n[-1]
    if count1 > count0:
        n += "0"
    else:
        n += "1"

    count0 = n.count("0")
    count1 = n.count("1")
    if count1 == count0:
        n += n[-1]
    if count1 > count0:
        n += "0"
    else:
        n += "1"

    n = int(n, 2)
    if n % 2 == 0 and n % 4 != 0:
        print(i)

#KEGE 4648
s = "2" * 55 + "3" * 44 + "1" * 33
while ("222" in s) or ("333" in s) or ("111" in s):
    if "222" in s:
        s = s.replace("222", "11", 1)
        if "222" in s:
            s = s[::-1]
            s = s.replace("222", "11", 1)
            s = s[::-1]
    elif "111" in s:
        s = s.replace("111", "3", 1)
    else:
        s = s.replace("333", "1", 1)
print(s)

#KEGE 642
s = "2" + "5"*81
while ("25" in s) or ("355" in s) or ("4555" in s):
    if "25" in s:
        s = s.replace("25", "4", 1)
    if "355" in s:
        s = s.replace("355", "2", 1)
    if "4555" in s:
        s = s.replace("4555", "3", 1)
print(s)

#56
s = "2" + "5" * 81
while ("25" in s) or ("355" in s) or ("4555" in s):
    if "25" in s:
        s = s.replace("25", "4", 1)
    if "355" in s:
        s = s.replace("355", "2", 1)
    if "4555" in s:
        s = s.replace("4555", "3", 1)
print(s)
"""

# 5667
# for n in range(1, 100):
#     s = 15*"3" + 18*"2" + n*"1"
#     while ("31" in s) or ("33" in s) or ("21" in s):
#         if "31" in s:
#             s = s.replace("31", "123", 1)
#         if "33" in s:
#             s = s.replace("33", "211", 1)
#         if "21" in s:
#             s = s.replace("21", "1", 1)
#     r = int(s)
#     summ = 0
#     while r > 0:
#         summ += r % 10
#         r //= 10
#     if summ > 24:
#         print(n)

# 5630
# for n in range(1, 3000):
#     s = ">" + 16*"1" + n*"2" + 16*"3"
#     while (">1" in s) or (">3" in s) or (">2" in s):
#         if (">1" in s):
#             s = s.replace(">1", "1>", 1)
#         if (">3" in s):
#             s = s.replace(">3", ">2", 1)
#         if (">2" in s):
#             s = s.replace(">2", ">1", 1)
#     summ = s.count("1") + s.count("2") + s.count("3")
#     f = 1
#     for i in range(2, 100):
#         if (summ % i == 0) and (summ != i):
#             f = 0
#             break
#     if f == 1:
#         print(n)

# 5287
# for n in range(1, 40):
#     s = n*"0"+"1"
#     while "01" in s:
#         if "1" in s:
#             s = s.replace("1", "10", 1)
#         if "01" in s:
#             s = s.replace("01", "1000", 1)
#     if 100 <= s.count("0") < 1000:
#         print(n, s.count("0"))

# c = 0
# for n in range(3, 51):
#     s = ">" + "1"*n + "2"*n + "3"*n
#     while ">1" in s or ">2" in s or ">3" in s:
#         if ">1" in s:
#             s = s.replace(">1", "22>3", 1)
#         if ">2" in s:
#             s = s.replace(">2", "2>", 1)
#         if ">3" in s:
#             s = s.replace(">3", "11>2", 1)
#     s = s.replace(">", "", 1)
#     summ = sum(int(x) for x in s)
#     if summ % 7 == 0:
#         c+=1
#     print(c)

# 11
# s = 70*"8"
# while "2222" in s or "8888" in s:
#     if "2222" in s:
#         s = s.replace("2222", "88", 1)
#     else:
#         s = s.replace("8888", "22", 1)
# print(s)

# 56
# s = "2" + 81*"5"
# while "25" in s or "355" in s or "4555" in s:
#     if "25" in s:
#         s = s.replace("25", "4", 1)
#     if "355" in s:
#         s = s.replace("355", "2", 1)
#     if "4555" in s:
#         s = s.replace("4555", "3")
# print(s)

# 375
# s = "1"+ 33*"0"
# while "1" in s or "100" in s:
#     if "100" in s:
#         s = s.replace("100", "0001", 1)
#     else:
#         s = s.replace("1", "00", 1)
# print(s.count("0"))

# 645
# s = 46*"1" + 31*"2"
# while "1111" in s:
#     s = s.replace("1111", "2", 1)
#     s = s.replace("2222", "1", 1)
# print(s)

# 648
# for i in range(1, 51):
#     s = i*"6"
#     while "66" in s:
#         s = s.replace("66", "1", 1)
#         s = s.replace("11", "2", 1)
#         s = s.replace("22", "6", 1)
#     if s == "21":
#         print(i)

# 649
# s = ">" + 11*"1" + 12*"2" + 30*"3"
# while ">1" in s or ">2" in s or ">3" in s:
#     if ">1" in s:
#         s = s.replace(">1", "22>", 1)
#     if ">2" in s:
#         s = s.replace(">2", "2>", 1)
#     if ">3" in s:
#         s = s.replace(">3", "1>", 1)
# s = s.split(">")
# s = s[0]+s[1]
# print(sum(int(x) for x in s))

# s = 333*"7"
# while "66" in s or "77777" in s:
#     if "66" in s:
#         s = s.replace("66", "7", 1)
#     else:
#         s = s.replace("77777", "676676", 1)
# print(s, sum(int(x) for x in s))

# for i in range(1, 100):
#     s= "0" + "1"*i + "2"*i + "0"
#     while "00" not in s:
#         if "011" in s:
#             s = s.replace("011", "101", 1)
#         else:
#             s = s.replace("01", "40", 1)
#             s = s.replace("02", "20", 1)
#             s = s.replace("0222", "1401", 1)
#     if s.count("1") == 6 and s.count("2") == 9:
#         print(s.count("4"))

# 6604
# for m in range(1, 20):
#     s = ">" + 15*"1" + 35*"2" + m*"3"
#     while ">1" in s or ">2" in s or ">3" in s:
#         if ">1" in s:
#             s = s.replace(">1", "2>", 1)
#         if ">2" in s:
#             s = s.replace(">2", "3>", 1)
#         if ">3" in s:
#             s = s.replace(">3", "11>", 1)
#     c = 0
#     j = int(s[:-1])
#     for i in range(2, j-1):
#         if j % i == 0:
#             c += 1
#     if c == 3:
#         print(m)

# 7614
# for n in range(4, 50):
#     s = "3"+n*"5"
#     while "25" in s or "355" in s or "555" in s:
#         if "25" in s:
#             s = s.replace("25", "32", 1)
#         if "355" in s:
#             s = s.replace("355", "25", 1)
#         if "555" in s:
#             s = s.replace("555", "3", 1)
#     if sum(int(x) for x in s) == 17:
#         print(n)

# 7591
# for i in range(4, 50):
#     s = "3" + "5"*i
#     while "25" in s or "355" in s or "555" in s:
#         if "25" in s:
#             s = s.replace("25", "3", 1)
#         if "355" in s:
#             s = s.replace("355", "52", 1)
#         if "555" in s:
#             s = s.replace("555", "23", 1)
#     if sum(int(x) for x in s) == 27:
#         print(i)

# 7814
# for n in range(6, 80):
#     s = "2" + "4"*n
#     while "14" in s or "244" in s or "444" in s:
#         if "14" in s:
#             s = s.replace("14", "2", 1)
#         if "244" in s:
#             s = s.replace("244", '14', 1)
#         if "444" in s:
#             s = s.replace("444", "21", 1)
#     if sum(int(x) for x in s) > 20:
#         print(n)

# ans = []
# for i in range(49, 90):
#     s = "0" + "1"*48 + "2"*i + "0"
#     while "00" not in s:
#         s = s.replace("02", "101", 1)
#         s = s.replace("11", "2", 1)
#         s = s.replace("012", "30", 1)
#         s = s.replace("010", "00", 1)
#     summ = sum(int(x) for x in s)
#     f = 1
#     for j in range(2, 101):
#         if summ % j != 0 and summ != j:
#             f = 1
#         else:
#             f = 0
#             break
#     if f:
#         ans.append(i)
# print(min(ans), ans)

# for i in range(4, 100):
#     s = "2" + "5"*i
#     while "25" in s or "355" in s or "555" in s:
#         if "25" in s:
#             s = s.replace("25", "5", 1)
#         if "355" in s:
#             s = s.replace("355", "52", 1)
#         if "555" in s:
#             s = s.replace("555", "3", 1)
#     if sum(int(x) for x in s) == 17:
#         print(i)

# 8368 -
# for n in range(100000, 1000000000):
#     s = "3" + "7"*n
#     while "37" in s or "577" in s or "777" in s:
#         if "37" in s:
#             s = s.replace("37", "7", 1)
#         if "577" in s:
#             s = s.replace("577", "73", 1)
#         if "777" in s:
#             s = s.replace("777", "5", 1)
#     summ = sum(int(x) for x in s)
#     ksumm = kn = []
#     for j in range(2, 101):
#         f = 1
#         if summ % j == 0:
#             f = 0
#         if n % j == 0 and f == 0:
#             f = 0
#             break
#     if f == 1:
#         print(n)






















