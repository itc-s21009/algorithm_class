data = [
    'kiyuna',
    'takazato',
    'nagamine',
    'oota',
    'asahi',
    'syunta',
    'seika',
    'kouichi'
]
print(data, 'もとのデータ')

for i in range(0, len(data) - 1):
    m = i
    for j in range(i+1, len(data)):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data, 'ソート後のデータ')