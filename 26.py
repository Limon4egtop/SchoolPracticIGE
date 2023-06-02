# 4712
# f = open("26_4712.txt")
# n = int(f.readline())
# m = [int(x) for x in f]
# m.sort(reverse=True)
# rez = [m[0]]
# kor = m[0]
# for i in range(1, len(m)):
#     if kor - m[i] >= 3:
#         rez.append(m[i])
#         kor = m[i]
# print(rez[-1], len(rez))        #51 2767

# 7826
# f = open("files/26_7826.txt")
# k, n = map(int, f.readline().split())
# # k,n = [2,6]
# m = []
# for _ in range(n):
#     m.append(list(map(int, f.readline().split())))
# # m = [(30,60), (61, 120), (79, 160), (79, 180), (100, 130), (170, 1440)]
# atr = [-1]*k
# c = 0
# xMax = -10000
# for i in range(n):
#     for j in range(k):
#         if atr[j] < m[i][0]:
#             atr[j] = m[i][1]
#             c+=1
#             xMax = max(j, xMax)
#             break
# print(c, xMax)

# f = open("26_7602.txt")
# k = int(f.readline())        #кол-во ячеек
# n = int(f.readline())        #окл-во пассажиров
# # k, n = 2, 5
# m = []
# for i in range(n):
#     a, b = f.readline().split()
#     m.append([int(a), int(b)])
# # m = [[30, 60], [40, 1000], [59, 60], [61, 1000], [1010, 1440]]
# box = [-1] * k
# m.sort()
# c = last = 0
# for i in range(n):
#     for j in range(k):
#         if box[j] < m[i][0]:
#             box[j] = m[i][1]
#             c += 1
#             last = j+1
#             break
# print(c, last)

# 8512
f = open("26_8512.txt")
k = int(f.readline())        #ячейки
n = int(f.readline())        #людей
m = []
for i in range(n):
    dop = f.readline().split()
    m.append([int(dop[0]), int(dop[1])])

# k = 2
# n = 5
# m = [[30,60], [40, 1000], [59, 60], [61, 1000], [1010, 1440]]

c = 0
kLast = 0
korob = [-1]*k
for i in range(n):
    for j in range(k):
        if korob[j] < m[i][0]:
            korob[j] = m[i][1]
            c += 1
            kLast = j
            break
print(c, kLast+1)




































