print('「A」のユニコード', ord('A'))
print('「あ」のユニコード', ord('あ'))
print('ユニコード33の文字', chr(33))
print('ユニコード12356の文字', chr(12356))
print('--------------------------')
while True:
    s = input('1文字を入力してください: ')
    if len(s) != 1:
        continue
    print(f'{s}のユニコード {ord(s)}')