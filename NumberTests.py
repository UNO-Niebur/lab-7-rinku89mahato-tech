#NumberTests.py
#Main

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def getFactors(num):
  """Returns a list of all factors of a given integer"""

  if num <= 0:
    raise ValueError
  
  factors = set()
  i = 1
  while i * i <= num:
    if num % i == 0:
      factors.add(i)
      factors.add(num// i)
    i += 1

  return sorted(factors)




def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p == 2:
    return True
  if p <= 1:
    return False
  if isEven(p):
    return False
  
  
  for div in range(3, p // 2, 2):
    if p % div == 0:
      return False
    
  return True

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))

# prime below 

def sum_primes_below(input_num):
    """ Return the sum of all prime numbers below the given limit"""
    sieve  = [True] * input_num
    sieve[0] = sieve[1] = False
    for f in range (2, int(input_num ** 0.5) + 1):
        if sieve[f]:
            for multiple in range(f * f, input_num, f):
              sieve[multiple] = False
        
            
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


if __name__ == '__main__':
    main()
