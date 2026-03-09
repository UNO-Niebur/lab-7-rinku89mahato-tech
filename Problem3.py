#Problem3.py
#LargestPrimefactor_600851475143

from NumberTests import isPrime
from NumberTests import getFactors

def main():
    number = 600851475143 # largest prime factor of provided number
    factors = getFactors(number)
    print(f"factors of {number}:{factors}")


if __name__ == '__main__':
    main()