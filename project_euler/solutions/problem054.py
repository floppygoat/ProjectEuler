from functools import reduce


def get_answer(filename="text_files/problem054.txt"):
    cards = file_to_cards(filename)
    p1cards = get_players_hands(cards, 0)
    p2cards = get_players_hands(cards, 5)
    wins = 0
    for p1_hand, p2_hand in zip(p1cards, p2cards):
        if p1_hand.winner(p2_hand):
            wins += 1
    return wins


class PokerHand:
    hand = []
    highest = []
    score = 0
    val_rank = 0

    def __init__(self, cards):
        self.hand = cards
        self.highest = sorted(list(map(lambda x: x.num, self.hand)), reverse=True)
        self.score, self.val_rank = self.calc_score()

    def winner(self, o_hand):
        if self.score > o_hand.score:
            return True
        if self.score < o_hand.score:
            return False
        if self.val_rank > o_hand.val_rank:
            return True
        if self.val_rank < o_hand.val_rank:
            return False
        for c, oc in zip(self.highest, o_hand.highest):
            if c > oc:
                return True
            if c < oc:
                return False
        return False

    def calc_score(self):
        same_suit = reduce((lambda x, y: x and y), list(map((lambda x: x.suit == self.hand[0].suit), self.hand)))
        consec = reduce((lambda x, y: x and y), [self.highest[i] == self.highest[i - 1] - 1 for i in range(1, 5)])
        if same_suit and consec:
            return 8, self.highest[0]

        def fours():
            if self.highest[1] == self.highest[2] and self.highest[2] == self.highest[3]:
                if self.highest[0] == self.highest[1] or self.highest[4] == self.highest[3]:
                    return [True, self.highest[2]]
            return [False, False]

        def threes():
            if len(list(filter(lambda x: x.num == self.hand[0].num, self.hand))) == 3:
                return [True, self.hand[0].num]
            if len(list(filter(lambda x: x.num == self.hand[1].num, self.hand))) == 3:
                return [True, self.hand[1].num]
            if len(list(filter(lambda x: x.num == self.hand[2].num, self.hand))) == 3:
                return [True, self.hand[2].num]
            return [False, False]

        def pairs():
            num_pair = 0
            pair_max = 0
            if self.highest[4] == self.highest[3] and self.highest[3] != self.highest[2]:
                pair_max = self.highest[3]
                num_pair += 1
            if self.highest[3] == self.highest[2] and \
                    self.highest[4] != self.highest[3] and \
                    self.highest[2] != self.highest[1]:
                pair_max = self.highest[2]
                num_pair += 1
            if self.highest[2] == self.highest[1] and \
                    self.highest[3] != self.highest[2] and \
                    self.highest[1] != self.highest[0]:
                pair_max = self.highest[1]
                num_pair += 1
            if self.highest[1] == self.highest[0] and self.highest[2] != self.highest[1]:
                pair_max = self.highest[0]
                num_pair += 1
            return num_pair, pair_max

        four = fours()
        if four[0]:
            return 7, four[1]
        three = threes()
        pair = pairs()
        if three[0] and pair[0] == 1:
            return 6, max(three[1], pair[1])
        if same_suit:
            return 5, self.highest[0]
        if consec:
            return 4, self.highest[0]
        if three[0]:
            return 3, three[1]
        if pair[0] == 2:
            return 2, pair[1]
        if pair[0] == 1:
            return 1, pair[1]
        else:
            return 0, self.highest[0]


class Card:
    """
    An object representing a playing card.
    Has a num corresponding to the ranking(eg. Jack has value 9, 2 has a value 0, Ace has a value 12),
    and a suit(H, C, D, S)
    """
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    num = 0
    suit = ""

    def __init__(self, s):
        self.num = self.values.index(s[0])
        self.suit = s[1]


def file_to_cards(filename):
    """
    Turns a file into list of Strings.  Assumes entries a split by a space " ".
    Gets rid of the character "\n".
    :param filename: File to get turned into list
    :return: list of strings.
    """
    f = open(filename, "r")
    strings = f.readlines()
    f.close()
    cards = []
    for x in range(0, len(strings)):
        cards.append(list(strings[x].replace("\n", "").split(" ")))
    return cards


def get_players_hands(cards, first):
    """

    :param cards: A matrix of Strings representing card
    :param first: What entry on each row to start reading the players cards from.
    :return: A list of PokerHands.
    """
    pcards = []
    for i in range(len(cards)):
        l1 = []
        for j in range(first, first + 5):
            l1.append(Card(cards[i][j]))
        pcards.append(PokerHand(l1))
    return pcards
