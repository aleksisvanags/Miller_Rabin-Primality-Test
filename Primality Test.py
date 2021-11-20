# Miller - Rabin Primality Test
# Aleksis Vanags
# 20/11/2021

import random


def main():
    print("This program uses the Miller - Rabin Primality Test.\nThis is done for seven rounds, because of this, the chance of a\nfalse output is one in five quadrillion.")
    while True:
        try:
            number = int(input("Enter your number:   "))
            print(f"{number} is prime!") if isPrime(number, 7) else print(f"{number} is not prime.")
        except ValueError:
            print("Please enter a number!")


def isPrime(n, k):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    main()
