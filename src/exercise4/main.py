num = input()
if num.isdigit():
    num = int(num)
    triangle = []

    for i in range(num):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    for r in triangle:
        print(*r)
else:
    print("Natural number was expected")
