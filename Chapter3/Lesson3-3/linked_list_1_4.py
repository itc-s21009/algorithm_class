MAX = 7
data = [None]*MAX
pointer = [None]*MAX
head = 0

def add_list(d):
    n = -1
    for i in range(MAX):
        if data[i] == None:
            n = i
            break
    if n == -1:
        print("データ領域に空きがありません")
        return False
    for i in range(MAX):
        if data[i] != None and pointer[i] == None:
            pointer[i] = n
            break
    data[n] = d
    pointer[n] = None
    print(f'データ {d} を追加しました')
    return True

def del_list(d):
    global head
    n = -1
    for i in range(MAX):
        if data[i] == d:
            n = i
            break
    if n == -1:
        print('そのデータは存在しません')
        return False
    if n != head:
        for i in range(MAX):
            if pointer[i] == n:
                pointer[i] = pointer[n]
    else:
        head = pointer[n]
        if head == None:
            head = 0
    data[n] = None
    pointer[n] = None
    print(f'データ {d} を削除しました')
    return True

def put_list():
    p = head
    while True:
        print(data[p], end=' → ')
        if pointer[p] == None:
            print('EOF')
            break
        p = pointer[p]

def replace_pointer(x, y):
    prevX, prevY = -1, -1
    for i in range(MAX):
        if pointer[i] == x:
            prevX = i
        if pointer[i] == y:
            prevY = i

    tmp = pointer[prevX]
    pointer[prevX] = pointer[prevY]
    pointer[prevY] = tmp

def replace(x, y):
    replace_pointer(x, y)
    print(data, pointer)
    replace_pointer(x + 1, y + 1)
    print(data, pointer)

def insert(data, position):
    
    pass

add_list('A')
add_list('B')
add_list('C')
add_list('D')
add_list('E')
add_list('F')
add_list('G')
# add_list('赤')
# add_list('橙')
# add_list('黄')
# add_list('緑')
# add_list('青')
# add_list('藍')
# add_list('紫')
put_list()
print(data, pointer)
while True:
    x, y = map(int, input('(x, y): ').split())
    replace(x, y)
    put_list()