def get_answer(power_limit=7):
    champernownes_constant = ""
    i = 1
    count = 0
    answer = 1
    while count < 10 ** power_limit:
        champernownes_constant += str(i)
        count += len(str(i))
        i += 1
    for i in range(power_limit):
        answer *= int(champernownes_constant[10 ** i - 1])
    return answer
