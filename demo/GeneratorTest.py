gen = (x*x for x in range(10))
print(gen)

for num in gen:
    print(gen)


def function1():
    for i in range(10):
        yield i


print(function1())


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# 引用函数
for x in fibon(10):
    print(x , end = ' ')

print('')
def oo():
    print('step 1')
    yield (1)
    print('step 2')
    yield (2)
    print('step 3')
    yield (3)


o = oo()
print(next(o))
print(next(o))
print(next(o))


print(' ')
def triangles( n ):         # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [ L [ i -1 ] + L [ i ] for i in range (len(L))]


n = 0
for t in triangles( 10 ):   # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break