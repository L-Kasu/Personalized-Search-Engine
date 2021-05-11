def sqr(n=int):
    acc = 0
    while True:
        if acc == n ** 2:
            return acc
        acc += 1


def fact(n):
    if n < 0:
        Exception("Invalid input")
    elif n > 1:
        return n * fact(n - 1)
    else:
        return 1


print("Fact(6) = " + str(fact(6)))
print("Fact(0) = " + str(fact(0)))
print("Fact(-6) = " + str(fact(-6)))

print(sqr(5))

print("Hello World!")
