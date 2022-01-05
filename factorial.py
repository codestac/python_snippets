# recursive
def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))

# iterative
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(fact(6))
			