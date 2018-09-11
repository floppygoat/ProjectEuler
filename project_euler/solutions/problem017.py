ONE = 3
TWO = 3
THREE = 5
FOUR = 4
FIVE = 4
SIX = 3
SEVEN = 5
EIGHT = 5
NINE = 4
TEN = 3
ELEVEN = 6
TWELVE = 6
THIRTEEN = 8
FOURTEEN = 8
FIFTEEN = 7
SIXTEEN = 7
SEVENTEEN = 9
EIGHTEEN = 8
NINETEEN = 8
TWENTY = 6
THIRTY = 6
FORTY = 5
FIFTY = 5
SIXTY = 5
SEVENTY = 7
EIGHTY = 6
NINETY = 6
HUNDRED = 7
AND = 3
THOUSAND = 8


def get_answer():
    """
    Brute force way to get the amount of letters for numbers one thousand and under.
    :return: Letters for all positive integers 1000 and below.
    """
    summation = 0
    summation += 100 * ONE + 90 * ONE + 1 * ONE
    summation += 100 * TWO + 90 * TWO
    summation += 100 * THREE + 90 * THREE
    summation += 100 * FOUR + 90 * FOUR
    summation += 100 * FIVE + 90 * FIVE
    summation += 100 * SIX + 90 * SIX
    summation += 100 * SEVEN + 90 * SEVEN
    summation += 100 * EIGHT + 90 * EIGHT
    summation += 100 * NINE + 90 * NINE
    summation += 10 * TEN
    summation += 10 * ELEVEN
    summation += 10 * TWELVE
    summation += 10 * THIRTEEN
    summation += 10 * FOURTEEN
    summation += 10 * FIFTEEN
    summation += 10 * SIXTEEN
    summation += 10 * SEVENTEEN
    summation += 10 * EIGHTEEN
    summation += 10 * NINETEEN
    summation += 100 * TWENTY
    summation += 100 * THIRTY
    summation += 100 * FORTY
    summation += 100 * FIFTY
    summation += 100 * SIXTY
    summation += 100 * SEVENTY
    summation += 100 * EIGHTY
    summation += 100 * NINETY
    summation += 9 * 100 * HUNDRED
    summation += 9 * 99 * AND
    summation += 1 * THOUSAND
    return summation
