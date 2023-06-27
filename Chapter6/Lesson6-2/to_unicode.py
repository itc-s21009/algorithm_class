def to_unicode(s):
    return ' '.join([str(ord(c)) for c in list(s)])


s = input('ユニコードに変換する文字列を入力: ')
l = to_unicode(s)
print(l)
