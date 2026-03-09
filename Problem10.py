#Problem10
#summation_of_primes
from NumberTests import sum_primes_below

def main():
    input_num = 2000000
    total= sum_primes_below(input_num)
    print(f"Sum_of_primes_below {input_num}: {total}")

if __name__ == '__main__':
 main()