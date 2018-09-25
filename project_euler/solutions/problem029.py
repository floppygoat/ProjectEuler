def get_answer(bound=100):
    powers = set()
    for a in range(2, bound + 1):
        for b in range(2, bound + 1):
            number = a ** b
            if number in powers:
                powers.add(number)
    return len(powers)
