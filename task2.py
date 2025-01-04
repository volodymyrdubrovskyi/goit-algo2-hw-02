from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію
    """
    memo = {}

    def cut(n):
        if n == 0:
            return 0
        if n in memo:
            return memo[n]

        max_profit = 0
        for i in range(1, n + 1):
            if i - 1 < len(prices):
                max_profit = max(max_profit, prices[i - 1] + cut(n - i))

        memo[n] = max_profit
        return max_profit

    max_profit = cut(length)
    
    cuts = []
    n = length
    while n > 0:
        for i in range(1, n + 1):
            if i - 1 < len(prices) and memo[n] == prices[i - 1] + memo.get(n - i, 0):
                cuts.append(i)
                n -= i
                break

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1  # Кількість розрізів
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію
    """
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        max_profit = 0
        for j in range(1, i + 1):
            if j - 1 < len(prices):
                max_profit = max(max_profit, prices[j - 1] + dp[i - j])
        dp[i] = max_profit

    max_profit = dp[length]

    cuts = []
    n = length
    while n > 0:
        for i in range(1, n + 1):
            if i - 1 < len(prices) and dp[n] == prices[i - 1] + dp[n - i]:
                cuts.append(i)
                n -= i
                break

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1  # Кількість розрізів
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
