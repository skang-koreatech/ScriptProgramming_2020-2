# 두 정수의 최대공약수(gcd)를 반환한다.
def gcd(n1, n2):
    gcd = 1 # gcd의 초깃값은 1이다.
    k = 2   # 가능한 gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # gcd를 갱신한다.
        k += 1

    return gcd # gcd를 반환한다.

def sum(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2
