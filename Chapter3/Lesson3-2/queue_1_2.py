MAX = 6
que = [0]*MAX
head = 0
tail = 0

def get_queue():
    i = head
    q = []
    while i%MAX != tail:
        q.append(que[i])
        i = (i+1)%MAX
    return q

def enqueue(d):
    global tail
    nt = (tail+1)%MAX

    if nt == head:
        print('待ち列がいっぱいです')
    else:
        que[tail] = d
        tail = nt
        count = len(get_queue())
        print(f'待ち時間: {count * 15}分')

def dequeue():
    global head
    if head == tail:
        print('取り出すデータが存在しません')
        return None
    else:
        d = que[head]
        que[head] = 0
        head = (head + 1)%MAX
        print(f'{d}が列から出ました')
        return d

for i in range(3):
    enqueue(i)

for i in range(2):
    dequeue()

enqueue(i)
