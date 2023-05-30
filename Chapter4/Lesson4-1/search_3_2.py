data = [
    ['佐藤', '000-0000-0000'],
    ['鈴木', '111-1111-1111'],
    ['高橋', '222-2222-2222'],
    ['田中', '333-3333-3333'],
    [None]
]
while True:
    s = input('検索する相手の名字は？: ')
    i = 0
    while data[i][0] != None and data[i][0] != s:
        i += 1
    if data[i][0] == None:
        print('その名は登録されていません')
        yn = input('登録しますか？(Y/n): ')
        if yn.lower() == 'y':
            num = input('番号を入力: ')
            data.remove([None])
            data.append([s, num])
            data.append([None])
            print(f'{s}さんの番号 {num} を登録しました')
    else:
        print(f'{data[i][0]}さんの番号は{data[i][1]}です')