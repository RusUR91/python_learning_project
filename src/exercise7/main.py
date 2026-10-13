N, M = list(map(int, input().split())) # Чтение размеров поля (N строк, M столбцов)

field = [list(map(int, input().split())) for _ in range(N)] # Чтение поля с монетами
max_money = [[0] * M for _ in range (N)]
max_money[0][0] = field[0][0]

for i in range(1, N): # Заполнение левого столбца (движение только вниз)
    max_money[i][0] = max_money[i - 1][0] + field[i][0]
for j in range(1, M):
    max_money[0][j] = max_money[0][j - 1] + field[0][j]

for i in range(1, N): # Заполнение остальных клеток (выбираем лучший путь: сверху или слева)
    for j in range(1, M):
        max_money[i][j] = max(max_money[i-1][j], max_money[i][j-1]) + field[i][j]

print(max_money[-1][-1]) # Вывод максимальной суммы в правой нижней клетке
