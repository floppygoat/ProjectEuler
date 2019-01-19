def get_answer(power=7_830_457, multiple=28433, amount_of_digits=10):
    """
    It is very simple (and fast) to ue Python's arbitrary precision if you want to calculate the last
    ten digits of this number.  You could also compute it more directly by creating a power function
    that takes the modulo argument as well.
    """
    return (multiple * pow(2, power, 10 ** amount_of_digits) + 1) % (10 ** amount_of_digits)
