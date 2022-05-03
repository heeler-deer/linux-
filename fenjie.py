# 大数分解
def factorization(n):
    i = 2
    ret = []
    while i * i <= n:
        while n % i == 0:
            ret.append(i)
            n //= i
        i += 1
    if n > 1:
        ret.append(n)
    return ret

if __name__ == '__main__':
    print(factorization(int(input())))
