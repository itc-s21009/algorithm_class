data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]

def search(data, key):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == key:
            return mid
        if data[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

key = int(input('number: '))
result = search(data, key)
if result == -1:
    print(f'{key}は見つかりません')
else:
    print(f'data[{result}]が{key}です')