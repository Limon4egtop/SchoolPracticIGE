"""#3228
line = ""
with open("*.txt", "r") as f:
    line = f.read()

line = line.replace("AC", "1").replace("AB", "1")
line = line.replace("A", " ").replace("B", " ").replace("C", " ")

print(max(len(x) for x in line.split()))

maxxx = 0
dop = 0
for i in range(len(line)):
    if line[i] == "1":
        dop += 1
    else:
        maxxx = max(maxxx, dop)
        dop = 0
print(maxxx)

#5171
s = open("*.txt").read()
c = 0
mx = 0

s = s.replace("CA", "!")

for i in range(len(s)):
    if s[i] == "!":
        c += 1
        mx = max(mx, c)
    else:
        c = 0
print(mx*2)     #*2 тк мы заменили 2 символа на 1

#5171 другое решение
s = open("*.txt").read()

s = s.replace("CA", "!").replace("A", " ").replace("B", " ").replace("C", " ")\
    .replace("D", " ").replace("E", " ").replace("F", " ").split()
print(max(len(x) for x in s)*2)

#5171 еще одно решение
print(max(len(x) for x in open("*.txt").read().replace("CA", "!").replace("A", " ").\
          replace("B", " ").replace("C", " ")\
    .replace("D", " ").replace("E", " ").replace("F", " ").split())*2)

#5223
s = open("*.txt").read()

s = s.replace("DD", "D D").split()
print(max(len(x) for x in s if "FE" in x))

#3018
s = open("*.txt").read()
print(s)
s = s.replace("A", "A A").split()
m = [x for x in s if (len(x) >= 17) and ("B" not in x)]
print(len(m))

#2499
s = open("*.txt").read()
c = 0
for i in range(len(s)-3):
    if (s[i] == "X") and (s[i+1] == "X") and (s[i+2] == "X") and (s[i+3] == "X"):
        c+= 1
print(c)

#2420
s = open("*.txt").read()
s = s.replace("C", " ").replace("D", " ").split()
print(max(len(x) for x in s))

#2419
s = open("*.txt").read()
s = s.replace("A", " ").replace("B", " ").split()
print(max(len(x) for x in s))
"""

# 5641
# f = open("*.txt").read()
# f = f.replace("NP", " ").replace("PO", " ").split()
# print(max(len(x) for x in f))

# # 6636
# f = open("*.txt").read()
# # f = '1234525345234'
# chet = ["0", "2", "4", "6", "8"]
# notChet = ["1", "3", "5", "7", "9"]
# z = 0
# zhis = 1
# c = 0
# cMax = -1000000
# for i in range(len(f)-1):
#     if z == 0:
#         if (f[i] in chet) and (f[i+1] in notChet):
#             z = 1
#             if zhis == 1:
#                 c += 1
#             else:
#                 c = 1
#             zhis = 0
#         else:
#             zhis = 0
#     else:
#         z = 0
#         zhis = 1
#     cMax = max(cMax, c)
# print(cMax)

# 2419
# s = open("files_24/24_2419.txt").read()
# print(max(len(c) for c in s.replace("A", " ").replace("B", " ").split()))

# 2420
# s = open("files_24/24_2420.txt").read()
# print(max(len(c) for c in s.replace("C", " ").replace("D", " ").split()))

# 2421
# s = open("files_24/24_2421.txt").read()
# print(max(len(c) for c in s.replace("D", " ").split()))

# 865
# s = open("files_24/24_865.txt").read()
# print(max(len(c) for c in s.replace("C", " ").replace("F", " ").split()))

# 2426
# s = open("files_24/24_2426.txt").read()
# print(max(len(c) for c in s.replace("A", " ").replace("B", " ").replace("C", " ").split()))

# 1040
# s = open("files_24/24_1040.txt").read()
# c = m = 1
# for i in range(len(s)-1):
#     if (s[i] in "0123456789") and (s[i+1] in "0123456789"):
#         c += 1
#         m = max(c, m)
#     else:
#         c = 1
# print(m)

# 1428
# s = open("files_24/24_1428.txt").read()
# print(max(len(c) for c in s.replace("XY", "X Y").replace("XZ", "X Z").split()))

# 1975
# s = open("files_24/24_1975.txt").read()
# print(max(len(c) for c in s.replace("PP", "P P").split()))

# 1302
# s = open("files_24/24_1302.txt").read()
# print(max(len(c) for c in s.replace("XZZY", "XZZ ZZY").split()))

# 21
# s = open("files_24/24_21.txt").read()
# c = m = 1
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         c += 1
#         m = max(m,c)
#     else:
#         c = 1
# print(m)

# 2422
# s = open("files_24/24_2422.txt").read()
# c = m = 1
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         c+=1
#         m = max(c,m)
#     else:
#         c = 1
# print(m)

# 2423
# s = open("files_24/24_2423.txt").read()
# c = m = 1
# for i in range(len(s) - 1):
#     if s[i] < s[i+1]:
#         c += 1
#         m = max(c,m)
#     else:
#         c = 1
# print(m)

# 2427
# s = open("files_24/24_2427.txt").read()#.lower()
# c = m = 1
# posl = []
# fullPosl = []
# for i in range(len(s)-1):
#     if s[i] > s[i+1]:
#         c += 1
#         m = max(c,m)
#         if posl == None:
#             posl.append(s[i])
#             posl.append(s[i+1])
#         else:
#             posl.append(s[i + 1])
#     else:
#         fullPosl.append(posl)
#         posl = []
#         c = 1
# print(m, max(len(c) for c in fullPosl))

# 4710
# s = open("24_4710.txt").read()
# s = s.replace("A", "1").replace("O", "1").replace("C", "2").replace("D", "2").replace("F","2")\
#     .replace("21", "*").replace("2"," ").replace("1"," ")
# print(max(len(x) for x in s.split()))
# # решение для конченых безумцев
# print(max(len(x) for x in open("24_4710.txt").read().replace("A", "1").replace("O", "1").replace("C", "2").replace("D", "2").replace("F","2").replace("21", "*").replace("2"," ").replace("1"," ").split()))

# 4642
# print(max(len(x) for x in open("files_24/24_4642.txt").read().replace("B","A").replace("2","1").replace("A1","*").replace("A"," ").replace("1", " ").split()))

# 6094
# print(max(len(x) for x in open("*.txt").read().replace("XYZY", "XYZ YZY").replace("Z", "X").replace("XY", "*").replace("X", " ").replace("Y", " ").split()))

# 3019
# s = open("24_3019.txt").read().replace("A", " A").replace("B", "B ").split()
# c = 0
# for x in s:
#     if len(x) <= 15 and x.count("F") >= 1 and x.count("A") == 1 and x.count("B") == 1:
#         c+=1
# print(c)

# 1145
# print(min(len(x)+2 for x in open("files_24/24_1145.txt").read().replace("D", " ").split()))

# 1146
# print(min(len(x) for x in open("files_24/24_1146.txt").read().replace("A", " ").replace("B", " ").replace("C", " ").
#           replace("E", " ").replace("F", " ").split()))

# 2250
# s = open("files_24/24_2250.txt").read().split("A")
# maxxx = -100000000000
# for i in range(len(s)-1):
#     maxxx = max(maxxx, len(s[i]+"A"+s[i+1]))
# print(maxxx)

# 2251
# s = open("files_24/24_2251.txt").read().split("D")
# m = -100000
# for i in range(len(s)-2):
#     m = max(m, len(s[i]+"D"+s[i+1]+"D"+s[i+2]))
# print(m)

# 66
# print(max(len(x) for x in open("files_24/24_66.txt").read().replace("KOT", "*").replace("K", " ")
#           .replace("O", " ").replace("T", " ").split()))

# 4602
# print(max(len(x) for x in open("files_24/24_4602.txt").read().replace("O", "A").replace("C","B").replace("D","B")
#           .replace("BA", "*").replace("A", " ").replace("B", " ").split()))

# m = [x[:-2] for x in open("22.txt").readlines()]
# rez = []
# for strok in m:
#     strok = strok.replace("A", " A").split()
#     print(strok)
#     for x in "QWERTYUIOPASDFGHJKLZXCVBNM":
#         break

# 7624 -
# f = open("24_7624.txt").read()
# # f = f.replace("Y", "X").replace("Z", "X").replace("XX", "*").replace("X", " ").split()
# # msax = -100000
# # for i in range(len(f)-1):
# #     if f[i].count("*") + f[i+1].count("*") == 0:
# #         msax = max(msax, len(f[i]) + len(f[i+1]))
# #     elif f[i].count("*") > 0:
# #         msax = max(msax, len(f[i]))
# #         f[i] = f[i].replace("*","")
# #     elif f[i+1].count("*") > 0:
# #         msax = max(msax, len(f[i+1]))
# #         f[i+1] = f[i+1].replace("*","")
# # print(msax)
# f = f.replace("Y","X").replace("Z","X").replace("XX", "X X").split()
# print(max(len(x) for x in f))

# print(max(len(x) for x in open("24_7624.txt").read().replace("Y","X").replace("Z","X").replace("XX", "X X").split()))

# 7600
# f = open("24_7600.txt").read()
# f = f.replace("R","Q").replace("S", "Q").replace("QQ", "Q Q").split()
# print(max(len(x) for x in f))

# 7824
# f = open("files/24_7824.txt").read().replace("B", "A").replace("C", "A").replace("AA", "A A").split()
# print(max(len(x) for x in f))

# f = open("22.txt").read().replace("B", " ").replace("A", " ").replace("C", " ").split()
# print(max(len(x) for x in f))

# f = open("1_24.txt").read().replace("B", "A").replace("C", "A").replace("AA", "A A").split()
# print(max(len(x) for x in f))

# 8510
# f = open("24_8510.txt").read().replace("O", "N").replace("P", "N")
# while "NN" in f:
#     f = f.replace("NN", "N N")
# f = f.split()
# print(max(len(x) for x in f))

# 8959
# f = open("24_8959.txt").read().replace("EA", "**").replace("NPC", "***")
# for x in "QWERTYUIOPASDFGHJKLZXCVBNM":
#     f = f.replace(x, " ")
# f = f.split()
# print(max(len(y) for y in f))

# f = open("24.txt").read()
# f = f.replace("B", "A").replace("C", "A")
# while "AA" in f:
#     f = f.replace("AA", "A A")
# f = f.split()
# c = 0
# for x in f:
#     if len(x) > 2:
#         c += 1
# print(c)

# f = open("24.txt").read()
# for a in "QWERTYUIOPASDFGHJKLZXCVBNM":
#     f = f.replace(a, f" {a} ")
# f = f.split()
# maxLen = -10000000
# c = 0
# fLast = ""
# for i in range(len(f)):
#     if fLast == f[i]:
#         c += 1
#     else:
#         maxLen = max(maxLen, c)
#         c = 0
#         fLast = f[i]
# print(maxLen)

# f = open("24.txt").read()
# for x in "1234567890":
#     f = f.replace(x, f' {x} ')
# f = f.split()
# maxLenStr = -1
# # dgvhbjn = ""
# # iiii = 0
# # print(f[:100])
# for i in range(len(f)-2):
#     if f[i] in "1234567890" and f[i+2] in "1234567890" and f[i+1] not in "1234567890":
#         if int(f[i]) % 2 != int(f[i+2]) % 2:
#             maxLenStr = max(maxLenStr, len(f[i+1]))
#             # if len(f[i+1]) == 47:
#             #     print(f[i], f[i+1], f[i+2])
#     # if len(f[i]) > len(dgvhbjn):
#     #     dgvhbjn = f[i]
#     #     iiii = i
# print(maxLenStr+2)
# # print(len(dgvhbjn), iiii)






















