def read_matrix_from_file(filename="input.txt"):
    with open(filename, "r") as f:
        matrix = [list(map(int, line.split())) for line in f if line.strip()]
    return matrix

def rec(matrix, x, y, n, stats): #Рекурсивно обходит фигуру, затирая единицы нулями и обновляя статистику.
    if x < 0 or y < 0 or x >= n or y >= n or matrix[x][y] == 0:
        return
    # Помечаем как посещённое (стираем)
    matrix[x][y] = 0
    # Обновляем статистику
    stats["count"] += 1
    stats["min_row"] = min(stats["min_row"], x)
    stats["max_row"] = max(stats["max_row"], x)
    stats["min_col"] = min(stats["min_col"], y)
    stats["max_col"] = max(stats["max_col"], y)
    # Рекурсивный обход 4 соседей
    rec(matrix, x + 1, y, n, stats)
    rec(matrix, x - 1, y, n, stats)
    rec(matrix, x, y + 1, n, stats)
    rec(matrix, x, y - 1, n, stats)

def main():
    matrix = read_matrix_from_file()
    n = len(matrix)
    squares = 0
    circles = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                # Нашли новую фигуру
                stats = {
                    "count": 0,
                    "min_row": i,
                    "max_row": i,
                    "min_col": j,
                    "max_col": j,
                }
                rec(matrix, i, j, n, stats)
                # Ожидаемая площадь квадрата = ширина * высота
                height = stats["max_row"] - stats["min_row"] + 1
                width = stats["max_col"] - stats["min_col"] + 1
                expected_area = height * width
                if expected_area == stats["count"]:
                    squares += 1
                else:
                    circles += 1

    print(squares, circles)

if __name__ == "__main__":
    main()

