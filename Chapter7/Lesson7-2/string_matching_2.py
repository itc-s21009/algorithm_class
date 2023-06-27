text = "I'm learning Python. It's interesting!"
pattern = "Python"
tn = len(text)
pn = len(pattern)
flg = False
flg_2 = False
p = 0

while p <= tn-pn:
    c = 0
    for i in range(pn):
        if text[p+i] == pattern[i]:
            c += 1
    if c == pn:
        flg = True
        break
    if c >= pn*0.75:
        flg_2 = True
        break
    p += 1

print(text)
if flg == True:
    print(f'{str(p+1)}文字目に{pattern}があります')
elif flg_2 == True:
    print(f'{str(p+1)}文字目に類似する文字列が見つかりました')
else:
    print(f'{pattern}は見つかりませんでした')