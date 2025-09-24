import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    '''Визначає кількість монет для видачі решти за допомогою жадібного алгоритму'''
    result = {}

    for coin in coins:
        if amount >= coin:
            # Скільки монет можна взяти, не перевищивши залишок
            count = amount // coin

            # Додаємо номінал монети та її кількість до нашого словника результатів
            result[coin] = count

             # Зменшуємо загальний залишок суми на вартість щойно виданих монет
            amount -= coin * count

    return result

def find_min_coins(amount):
    '''Визначає мінімальну кількість монет для видачі решти за допомогою динамічного програмування'''
    # min_coins[i] зберігає мінімальну кількість монет для суми i
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # coin_used[i] зберігає останню додану монету для суми i
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Відновлюємо набір монет з отриманих даних
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result

if __name__ == "__main__":
    # Приклад вирішення з задачі
    print(f"Жадібний алгоритм для суми 113: {find_coins_greedy(113)}")
    print(f"Алгоритм динамічного програмування для суми 113: {find_min_coins(113)}")

    # Додаткові суми для тестування
    test_amounts = [113, 987, 8654, 32768, 100000, 2300000]

    # Виконання тестів
    print(f"{'Сума':<10} | {'Жадібний (час, сек)':<25} | {'Динамічний (час, сек)':<25}")
    print("-" * 65)

    for amount in test_amounts:
        # Вимірювання часу для жадібного алгоритму
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
        
        # Вимірювання часу для динамічного програмування
        dp_time = timeit.timeit(lambda: find_min_coins(amount), number=100)
        
        print(f"{amount:<10} | {greedy_time:<25.8f} | {dp_time:<25.8f}")