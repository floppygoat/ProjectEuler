from project_euler.library import list_primes, is_prime


def get_answer(ratio=0.1):
    primes = list_primes(100_000)
    i = 1
    count = 1
    prime_count = 0
    current_spiral_size = 2
    while True:
        for _ in range(4):
            i += current_spiral_size
            if is_prime(i, primes):
                prime_count += 1
        count += 4
        if prime_count / count < ratio:
            return current_spiral_size + 1
        current_spiral_size += 2
