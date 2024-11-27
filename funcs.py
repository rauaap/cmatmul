listcomp_matmul = lambda a, b: [
    [
        sum(a[y][i] * b[i][x] for i in range(len(b)))
        for x in range(len(a))
    ] for y in range(len(a))
]

def loop_matmul(a, b):
    alen, blen = len(a), len(b)
    ret = [[None for _ in range(alen)] for _ in range(alen)]
    for y in range(alen):
            for x in range(alen):
                    ret[y][x] = sum(a[y][i] * b[i][x] for i in range(blen))
    return ret
