def sqr(n=int):
    acc = 0
    while(True):
        if (acc == n**2):
            return acc
        acc += 1

print(sqr(5))