def get_answer(power=7_830_457, multiple=28433, amount_of_digits=10):
    return (multiple * pow(2, power, 10 ** amount_of_digits) + 1) % (10 ** amount_of_digits)