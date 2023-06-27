def to_string(unicode_list):
    return ''.join([chr(i) for i in unicode_list])


l = list(map(int, input('ユニコード番号をスペース区切りで入力: ').split(' ')))
s = to_string(l)
print(s)
