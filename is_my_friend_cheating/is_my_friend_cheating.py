def removNb(n):
    ret = []
    sum = (1 + n) / 2 * n
    for a in range(1, n+1):
        if ((sum - a) % (a + 1) == 0) and ((sum - a) // (a + 1) <= n) and (a != (sum - a) // (a + 1)):
            ret.append((a, int((sum - a) // (a + 1))))
    return ret
