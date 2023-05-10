# 5284
# f = open("*.csv")
# c = 0
# for s in f:
#     m = [int(x) for x in s.split(";")]
#     m.sort()
#     m3 = [x for x in m if m.count(x) == 3]
#     m1 = [x for x in m if m.count(x) == 1]
#     y = [(m[0]+m[-1]) ** 2 > m[1]**2 + m[2]**2 + m[3]**2 + m[4]**2, len(m3) == 3 and len(m1) == 3]
#     if any(y):
#         c+=1
# print(c)

# 5126
# f = open("*.csv")
# c = 0
# for s in f:
#     m = [int(x) for x in s.split(";")]
#     m.sort()
#     m3 = [x for x in m if m.count(x) == 3]
#     m1 = [x for x in m if m.count(x) == 1]
#     y = [sum(m1)/3 <= sum(m3), len(m3) == 3, len(m1) == 3]
#     if all(y):
#         c += 1
# print(c)


# f = open("*.csv")
# c = 0
# for s in f:
#     m = [int(x) for x in s.split(";")]
#     m.sort()
#     m3 = [x for x in m if m.count(x) == 3]
#     m1 = [x for x in m if m.count(x) == 1]
#     y = [len(m3) == 3, len(m1) == 3, sum(m1)/3 <= sum(m3)]
#     if all(y):
#         c += 1
# print(c)

# 5489
# f = open("9_5489.csv")
# c = 0
# for s in f:
#     m = [int(x) for x in s.split(";")]
#     m1 = [x for x in m if m.count(x) == 1]
#     mChet = [x for x in m if x % 2 == 0]
#     y = [len(m1) == 5, sum(mChet) < sum(m)-sum(mChet), len(mChet) > len(m)-len(mChet)]
#     if all(y):
#         c+=1
# print(c)

































