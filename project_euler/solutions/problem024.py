def get_answer(nth=1_000_000):
    count = 0
    number = [None] * 10
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in digits:
        digits.remove(a)
        number[0] = a
        for b in digits:
            digits.remove(b)
            number[1] = b
            for c in digits:
                digits.remove(c)
                number[2] = c
                for d in digits:
                    digits.remove(d)
                    number[3] = d
                    for e in digits:
                        digits.remove(e)
                        number[4] = e
                        for f in digits:
                            digits.remove(f)
                            number[5] = f
                            for g in digits:
                                digits.remove(g)
                                number[6] = g
                                for h in digits:
                                    digits.remove(h)
                                    number[7] = h
                                    for i in digits:
                                        digits.remove(i)
                                        number[8] = i
                                        for j in digits:
                                            digits.remove(j)
                                            number[9] = j
                                            count += 1
                                            if count == nth:
                                                return number
                                            digits.append(j)
                                            digits.sort()
                                        digits.append(i)
                                        digits.sort()
                                    digits.append(h)
                                    digits.sort()
                                digits.append(g)
                                digits.sort()
                            digits.append(f)
                            digits.sort()
                        digits.append(e)
                        digits.sort()
                    digits.append(d)
                    digits.sort()
                digits.append(c)
                digits.sort()
            digits.append(b)
            digits.sort()
        digits.append(a)
        digits.sort()
    return 0
