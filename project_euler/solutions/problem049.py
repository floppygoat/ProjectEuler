from math import sqrt


def get_answer():
    primes = find_primes(10_000)
    for i in range(0, len(primes)):
        if len(str(primes[i])) == 4:
            for j in range(i + 1, len(primes)):
                if permutation(primes[i], primes[j]):
                    try:
                        k = primes.index(2 * primes[j] - primes[i])
                        if permutation(primes[i], primes[primes.index(2 * primes[j] - primes[i])]):
                            if primes[i] != 1487:
                                return primes[i] * (10 ** 8) + primes[j] * (10 ** 4) + primes[k]
                    except ValueError:
                        pass
    return None


def permutation(number1, number2):
    digits1, digits2 = [], []
    while number1 > 0 and number2 > 0:
        digits1.append(number1 % 10)
        digits2.append(number2 % 10)
        number1, number2 = number1 // 10, number2 // 10
    check = False
    while len(digits1) != 0:
        for j in range(0, len(digits2)):
            if digits1[0] == digits2[j]:
                del digits1[0]
                del digits2[j]
                check = True
                break
        if not check:
            return check
        check = False
    return True


def find_primes(limit):
    sieve = [True] * (limit // 2)
    i = 1
    bound = sqrt(limit)
    while (2 * i) < bound:
        if sieve[i]:
            j = (3 * i) + 1
            while (2 * j) + 1 < limit:
                sieve[j] = False
                j += (2 * i) + 1
        i += 1
    i = 1
    primes = [2]
    while i < len(sieve):
        if sieve[i]:
            primes.append((i * 2) + 1)
        i += 1
    return primes
