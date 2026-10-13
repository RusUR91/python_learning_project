def calculate_derivative(coeffs, x):
    derivative_value = 0
    degree = len(coeffs) - 1 # старшая степень многочлена

    for i in range(degree):  # i от 0 до degree-1, проходим по всем членам, кроме свободного
        power = degree - i  # текущая степень (от N до 1)
        derivative_value += coeffs[i] * power * (x ** (power - 1))  # производная члена: коэффициент * степень * x^(степень-1)

    return derivative_value

# Чтение входных данных
N, x = input().split()
N = int(N)  # степень многочлена
x = float(x)  # точка, в которой считаем производную

# Чтение коэффициентов (от старшей степени до свободного члена)
coeffs = []
for _ in range(N + 1):
    coeffs.append(float(input()))

# Вычисление и вывод результата
result = calculate_derivative(coeffs, x)
print(f"{result:.3f}")

