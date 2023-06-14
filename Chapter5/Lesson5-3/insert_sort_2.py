data = [9, 8, 3, 5, 0]
n = len(data)
print(data, 'もとのデータ')

for i in range(1, n):
    tmp = data[i]
    j = i
    while j > 0 and data[j - 1] > tmp:
        data[j] = data[j - 1]
        j = j - 1
    data[j] = tmp
    for k in range(n):
        if data[k] == tmp:
            print(f'\033[31m{data[k]}', end='\033[0m, ')
        else:
            print(data[k], end=', ')
    print()

print(data, 'ソート後のデータ')
