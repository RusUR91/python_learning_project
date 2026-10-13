original_num = int(input())
num = original_num
revers_num = 0
temp = num
while temp > 0:
    revers_num = revers_num * 10 + (temp % 10)
    temp //= 10

palindrom = (revers_num == original_num)
print('True' if palindrom else 'False')
