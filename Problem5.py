
from NumberTests import sum_primes_below

def main():
    limit = 2_000_000
    total= sum_primes_below(limit)
    print(f"Sum_of_primes_below {limit}: {total}")

if __name__ == '__main__':
 main()