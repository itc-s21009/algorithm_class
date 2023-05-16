size = 9
p = [True] * (size * size)
p[0] = False
p[1] = False
n = 2

def hyou():
    s = ''
    for i in range(size * size):
        if p[i] == True:
            s += '{:2d}, '.format(i)
        else:
            s += '／, '
        if i%size == size - 1:
            s += '\n'
    print(s)

def furui():
    global n
    for i in range(n+n, size * size, n):
        p[i] = False
    cnt = 0
    for i in range(size*size):
        if p[i] == False:
            cnt += 1
    print(f'{n}の倍数をふるい落としました 素数:{cnt}個')
    while n<size * size:
        n = n + 1
        if p[n] == True:
            break
while n < size:
    furui()
hyou()
