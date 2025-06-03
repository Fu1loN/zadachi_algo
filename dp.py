def lcs(str1, str2, dp_need=False):
    # Получаем длины строк
    m = len(str1)
    n = len(str2)
    
    # Создаем таблицу dp размером (m+1)x(n+1)
    # dp[i][j] будет содержать длину LCS для str1[0..i-1] и str2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Заполняем таблицу dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Восстанавливаем саму последовательность
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    if dp_need:
        return dp[m][n], ''.join(reversed(lcs)), dp
    # Возвращаем длину LCS и саму последовательность
    return dp[m][n], ''.join(reversed(lcs))

def main():
    # Пример использования
    str2 = "питекантроп"
    str1 = "кинотеатр"
    
    length, sequence, dp_table = lcs(str1, str2, dp_need=True)
    
    print(f"\nДлина наибольшей общей подпоследовательности: {length}")
    print(f"Наибольшая общая подпоследовательность: {sequence}")
    
    # Выводим таблицу для наглядности
    print("\nТаблица динамического программирования:")
    print(" " * 4 + " ".join(f"{c:3}" for c in str2))
    
    
    for i in range(len(str1) + 1):
        if i == 0:
            continue
        else:
            print(f"{str1[i-1]}", end=" ")
        print(" ".join(f"{x:3}" for x in dp_table[i][1:]))

if __name__ == "__main__":
    main() 