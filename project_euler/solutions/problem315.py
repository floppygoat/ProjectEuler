from project_euler.library import list_primes
import time

#    -----0-----
#    =         =
#    5         1
#    =         =
#    -----6-----
#    =         =
#    4         2
#    =         =
#    -----3-----


class Display:
    def __init__(self, display, display_count):
        self.display = display
        self.display_count = display_count


ZERO_DISPLAY = [True, True, True, True, True, True, False]
ONE_DISPLAY = [False, True, True, False, False, False, False]
TWO_DISPLAY = [True, True, False, True, True, False, True]
THREE_DISPLAY = [True, True, True, True, False, False, True]
FOUR_DISPLAY = [False, True, True, False, False, True, True]
FIVE_DISPLAY = [True, False, True, True, False, True, True]
SIX_DISPLAY = [True, False, True, True, True, True, True]
SEVEN_DISPLAY = [True, True, True, False, False, True, False]
EIGHT_DISPLAY = [True, True, True, True, True, True, True]
NINE_DISPLAY = [True, True, True, True, False, True, True]

DISPLAY = [Display(ZERO_DISPLAY, 6), Display(ONE_DISPLAY, 2), Display(TWO_DISPLAY, 5),
           Display(THREE_DISPLAY, 5), Display(FOUR_DISPLAY, 4), Display(FIVE_DISPLAY, 5),
           Display(SIX_DISPLAY, 6), Display(SEVEN_DISPLAY, 4), Display(EIGHT_DISPLAY, 7),
           Display(NINE_DISPLAY, 6)]


def get_answer(lower_bound=10_000_000, upper_bound=20_000_000):
    """
    For Sam's, the algorithm is simply two times the amount of LEDs of each number
    For Max's, the algorithm is the amount of LEDs of the first number,
                + the amount of LEDS of the last number,
                + the number of LEDs that are different between each number in the cycle

    Since the maximum value the second digit in the cycle is 64 (in this example), we calculate the full
    cycle for numbers up to 64, then for prime numbers between 10_000_000 and 20_000_000, once we know the
    second number in the cycle, simply add up the remaining amount of LEDs that will be displayed.

    The algorithm could be made much faster by making a mapping of the switch for each individual digit,
    as well as having a pre-made list of prime numbers
    """

    sams_transitions = 0
    maxs_transitions = 0

    transitions = []
    primes = list_primes(upper_bound)

    for num in range(0, 10):
        # S
        transitions.append([2 * DISPLAY[num].display_count,  # Sam's Clock.  Turn the digit on/off
                            DISPLAY[num].display_count])  # Max'x Clock.  Turn the digit off

    for num in range(10, 9 * len(str(upper_bound)) + 1):
        root = digital_root(num)
        on_off = transitions_on_off(num)
        switch = transitions_switch(num, root)

        transitions.append([2 * on_off + transitions[root][0],
                            switch + transitions[root][1]])

    for num in primes:
        if num < lower_bound:
            continue
        root = digital_root(num)
        on_off = transitions_on_off(num)
        switch = transitions_switch(num, root)
        sams_transitions += 2 * on_off + transitions[root][0]
        maxs_transitions += on_off + switch + transitions[root][1]

    return sams_transitions - maxs_transitions


def digital_root(num):
    root = 0
    x = num
    while x > 0:
        root += x % 10
        x //= 10
    return root


def transitions_on_off(x):
    transitions = 0
    while x > 0:
        transitions += DISPLAY[x % 10].display_count
        x //= 10
    return transitions


def transitions_switch(num1, num2):
    transitions = 0
    while num1 != 0 and num2 != 0:
        x, y = num1 % 10, num2 % 10
        num1 //= 10
        num2 //= 10
        for dis1, dis2 in zip(DISPLAY[x].display, DISPLAY[y].display):
            if dis1 != dis2:
                transitions += 1

    if num2 == 0:
        while num1 != 0:
            transitions += DISPLAY[num1 % 10].display_count
            num1 //= 10
        return transitions
    while num2 != 0:
        transitions += DISPLAY[num2 % 10].display_count
        num2 //= 10
    return transitions

