from functools import reduce


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

print('自然数をスペース区切りでいくつか入力してください')
l = map(int, input().split())
print('それらの数の最大公約数は', reduce(euclid, l))