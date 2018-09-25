def get_answer(nth=3):
    triangle_number, pentagonal_number, hexagonal_number = 1, 1, 1
    tnth, pnth, hnth = 1, 1, 1
    count = 0
    while True:
        if triangle_number == pentagonal_number and triangle_number == hexagonal_number:
            count += 1
            if count == nth:
                return triangle_number
            tnth += 1
            pnth += 1
            hnth += 1
            triangle_number = tnth * (tnth + 1) // 2
            pentagonal_number = pnth * (3 * pnth - 1) // 2
            hexagonal_number = hnth * (2 * hnth - 1)
        elif triangle_number <= pentagonal_number and triangle_number <= hexagonal_number:
            tnth += 1
            triangle_number = tnth * (tnth + 1) // 2
        elif pentagonal_number <= triangle_number and pentagonal_number <= hexagonal_number:
            pnth += 1
            pentagonal_number = pnth * (3 * pnth - 1) // 2
        else:
            hnth += 1
            hexagonal_number = hnth * (2 * hnth - 1)
