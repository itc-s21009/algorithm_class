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
    print(data)

print(data, 'ソート後のデータ')
