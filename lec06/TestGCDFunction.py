#from GCDFunction import gcd # gcd 함수를 임포트한다.
#import GCDFunction
from GCDFunction import gcd, sum
#from GCDFunction import *



# 사용자로부터 두 정수를 입력받는다.
n1 = eval(input("첫 번째 정수를 입력하세요: "))
n2 = eval(input("두 번째 정수를 입력하세요: "))

#print(n1, "와/과", n2, "의 최대공약수는", gcd(n1, n2), "입니다.")
#print(n1, "와/과", n2, "의 최대공약수는", GCDFunction.gcd(n1, n2), "입니다.")
print(n1, "와/과", n2, "의 최대공약수는", gcd(n1, n2), "입니다.")
print(n1, "와/과", n2, "의 합", sum(n1, n2), "입니다.")
