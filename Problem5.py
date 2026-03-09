
from NumberTests import sum_primes_below

def main():
    primes_limit = int(input("Enter the upper limit: "))
    total_sum = sum_primes_below(primes_limit)
    print("Sum_of_primes_below {limit}:  {total_sum}")

if __name__ == '__main__':
 main()