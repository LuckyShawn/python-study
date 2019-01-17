def sum(a, b):
    return a + b


print(sum(1, 2))

a = 10


def method(a):
    a = 20
    print('方法中：', a)


method(a)
print('调用方法后：', a)


def chagne_list(b):
    print('函数中一开始 b 的值：{}'.format(b))
    b.append(1000)
    print('函数中 b 赋值后的值：{}'.format(b))


b = [1, 2, 3, 4, 5]
chagne_list(b)
print('最后输出 b 的值：{}'.format(b))


def sum(num1, num2):
    # 两数之和
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError('参数类型错误')
    return num1 + num2


print(sum(1, 2))


def double(num1, num2):
    a = num1 + num2
    b = num1 - num2
    return a, b


a, b = double(3, 2)
print(a, b)
tuple1 = double(3, 2)
print(tuple1)


def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


print_user_info('shawn', 18, '女')
print_user_info('jack', 25)


print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))

#生成式
list1 = [ x * x for x in range(1, 10) ]
print(list1)

list2 = [x*x for x in range(1, 10) if x % 2 == 0]
print(list2)

list3 = [(x, y) for x in range(10) for y in range(10)]
print(list3)
