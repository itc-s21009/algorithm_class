data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
print(data, 'もとのデータ')

for i in range(len(data) - 1):
    mini = i
    for j in range(i + 1, len(data)):
        if data[mini] > data[j]:
            mini = j
    data[i], data[mini] = data[mini], data[i]

print(data, 'ソート後のデータ')
