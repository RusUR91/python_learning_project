num = int(input())
input_numbers = list(map(int, [input() for i in range(num)]))
final_score = 0
unique_numbers = []

for i in range(num):
    if input_numbers[i] not in unique_numbers:
        unique_numbers.append(input_numbers[i])
        final_score += 1
print(final_score)
