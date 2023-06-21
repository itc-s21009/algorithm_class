F = 99999
way = [
    [F, 3, 2, 5, F, F, F],
    [3, F, F, F, 7, F, F],
    [2, F, F, 2, F, 4, F],
    [5, F, 2, F, F, 1, F],
    [F, 7, F, F, F, 4, 5],
    [F, F, 4, 1, 4, F, 3],
    [F, F, F, F, 5, 3, F]
]
dist = [F]*7
flg = [0]*7
start = 0
p = start
dist[p] = 0
print(f'ノード{p}からの距離を探索します')

def f(n):
    return str(n) if n != 99999 else 'F'

for i in range(7):
    print(f'ノード{i}までの距離を探索')
    d = F
    for j in range(7):
        print(f'flg[{j}]={f(flg[j])}\tdist[{j}]={f(dist[j])}\td={f(d)}\tp={p}')
        if flg[j] == 0 and dist[j] < d:
            print(f'  変数を更新 (p={p}->{j}, d={f(d)}->{dist[j]})')
            p = j
            d = dist[j]
    print(f'flg[{p}] => 1')
    flg[p] = 1
    print('dist[p]\t\tway[p][k]\tdist[k]')
    for k in range(7):
        print(f'dist[{p}]={f(dist[p])}\tway[{p}][{k}]={f(way[p][k])}\tdist[{k}]={f(dist[k])}')
        if dist[p] + way[p][k] < dist[k]:
            print(f'  最短距離を更新 (dist[{k}]={f(dist[k])} -> {dist[p] + way[p][k]})')
            dist[k] = dist[p] + way[p][k]
    print(f'dist=[{", ".join(list(map(f,dist)))}]')

print('各ノードまでの距離')
for i in range(7):
    print(f'ノード{i}まで {dist[i]}')