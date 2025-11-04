#25
keys = input('alpha bravo charlie delta echo foxtrot golf를 입력하세요: ').split()
values = list(map(int, input('30 40 50 60 70 80 90을 입력하세요: ').split()))
a = dict(zip(keys, values))

del a['alpha']
del a['delta']

print(a)