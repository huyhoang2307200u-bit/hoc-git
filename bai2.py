import math
def phantichso(n):
    ds = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            ds.append(i)
            n //= i
    if n > 1:
        ds.append(n)
    return ds



if __name__ == "__main__":

    n = int(input("Nhap so can phan tich: "))
    print(phantichso(n))