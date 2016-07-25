import random
import copy

inf = float("inf")
dataCost = [[0, 30, 84, 56, inf, inf, inf, 75, inf, 80],
            [30, 0, 65, inf, inf, inf, 70, inf, inf, 40],
            [84, 65, 0, 74, 52, 55, inf, 60, 143, 48],
            [56, inf, 74, 0, 135, inf, inf, 20, inf, inf],
            [inf, inf, 52, 135, 0, 70, inf, 122, 98, 80],
            [70, inf, 55, inf, 70, 0, 63, inf, 82, 35],
            [inf, 70, inf, inf, inf, 63, 0, inf, 120, 57],
            [75, inf, 135, 20, 122, inf, inf, 0, inf, inf],
            [inf, inf, 143, inf, 98, 82, 120, inf, 0, inf],
            [80, 40, 48, inf, 80, 35, 57, inf, inf, 0]]
vec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cost(rote):
    c = 0.0
    pre = 0
    for i in rote:
        if i < 10 and pre < 10:
            c += dataCost[pre][i]
            pre = i
    c += dataCost[rote[9]][0]
    return c


def show(rote):
    print cost(rote)
    pre = 0
    for i in rote:
        if i == 0 or i > 9 or pre > 9:
            continue
        print str(pre) + " -> " + str(i) + " = " + str(dataCost[pre][i])
        pre = i
    print str(rote[9]) + " -> 0 = " + str(dataCost[rote[9]][0])


if __name__ == '__main__':
    best = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bestCost = inf
    for i in range(0, 10000000):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        vec[a], vec[b] = vec[b], vec[a]
        total = cost(vec)
        if bestCost > total != inf:
            best = copy.deepcopy(vec)
            bestCost = total
    show(best)
