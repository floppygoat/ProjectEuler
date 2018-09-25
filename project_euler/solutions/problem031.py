def get_answer(total=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    count = [1] + [0] * total
    for coin in coins:
        for i in range(coin, total + 1):
            count[i] += count[i - coin]
    return count[-1]


# ---------------------------------------------------------------


def coin_sums(total, count, coins):
    if total == 0:
        return count + 1
    elif total < 0:
        return count
    for coin in coins:
        count = coin_sums(total - coin, count, coins[coins.index(coin):len(coins)])
    return count


def problem31alt(total=200):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return coin_sums(total, 0, coins)
