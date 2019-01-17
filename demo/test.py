num = 10
if num > 0:
    print('Yes')
else:
    print('No')


str = 'a'
if str == 'a':
    print('a')
else:
    print('no a')

list = ['列表元素1',123,True]
print(list)
print(list[0])
print(list[0:2])
list[1] = 456;
print(list)
list.append('hello')
print(list)
del list[0]
print(list)
del list
print(list)

list1 = [1,2]
list2 = [3,'a']
list3 = list1 + list2
print(list3)
print((1 in list1))

for x in list3:
    print(x)

list4 = [1, 2, 3, 4, 5, 6]
print('长度：', len(list4))
print('最大值：', max(list4))
list4.insert(0, '123')
print(list4)
list4.pop()
print(list4)