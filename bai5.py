n = int(input())
res = 1

for i in range(1, n + 1):
    res *= i


    while res % 10 == 0:
        res //= 10

    res %= 100000000

print(res % 10)
