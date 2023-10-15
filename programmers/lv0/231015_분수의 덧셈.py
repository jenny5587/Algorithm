from fractions import Fraction
#분수표현 모듈
def solution(numer1, denom1, numer2, denom2):
    Fraction1 = Fraction(numer1,denom1)
    Fraction2 = Fraction(numer2,denom2)
    result = Fraction(numer1,denom1) + Fraction(numer2,denom2)
    answer = [result.numerator, result.denominator]
    return answer
