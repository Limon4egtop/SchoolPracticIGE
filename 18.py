from functools import lru_cache

f = [[int(x) for x in i.split(",")] for i in open("18_1.csv", 'r').readlines()]
res = []


@lru_cache(None)
def game(x, y, coins, chet_count):
    global f
    global res
    coins += f[y][x]
    if f[y][x] % 2 == 0:
        chet_count += 1

    if y < 18:
        game(x, y + 1, coins, chet_count)
        if x > 0:
            game(x - 1, y + 1, coins, chet_count)
        if x < 18:
            game(x + 1, y + 1, coins, chet_count)
    if y == 18:
        res.append((coins, chet_count))
        return


for x in range(19):
    game(x, 0, 0, 0)
res.sort(key=lambda x: x[0])
print(res[-1])