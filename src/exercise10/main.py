n, required_time = map(int, input().split()) # чтение количества аппаратов и требуемого времени работы

if n <= 0 or required_time <= 0:
    print("Error")
else:
    appliances = []  # список для хранения всех аппаратов
    error = False

    for _ in range(n): # чтение данных об аппаратах
        year, cost, work_time = map(int, input().split())
        if year <= 0 or cost <= 0 or work_time <= 0: # проверка корректности (все числа должны быть положительными)
            print("Error")
            error = True
            break
        appliances.append((year, cost, work_time))

    if not error:
        min_cost = float('inf') # минимальная стоимость (пока бесконечность)

        for i in range(n):
            for j in range(i + 1, n): # проверка: одинаковый год выпуска и суммарное время >= требуемому
                if (appliances[i][0] == appliances[j][0] and
                    appliances[i][2] + appliances[j][2] >= required_time): 
                    total_cost = appliances[i][1] + appliances[j][1]
                    if total_cost < min_cost: # обновляем минимальную стоимость
                        min_cost = total_cost

        if min_cost != float('inf'):
            print(min_cost)
        else:
            print("Error")
