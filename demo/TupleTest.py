# 二、tuple（元组）
# 另一种有序列表叫元组：tuple 。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改。那么不能修改是指什么意思呢？
#
# tuple 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，
# insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。那么为什么要有 tuple 呢？
# 那是因为 tuple 是不可变的，所以代码更安全。所以建议能用 tuple 代替 list 就尽量用 tuple 。

tuple1 = ('shawn', 'jack', 123)
tuple2 = 'shawn', 'jack', 123
tuple3 = ()
tuple4 = (123,)  # 必须在后面加上，才是元组
list1 = [tuple1, tuple2, tuple3, tuple4]
print(list1)

list2 = [1, 2, 'a']
tuple5 = (list2, 'first');
print(tuple5)
print(tuple5 * 3)
len(tuple5)
tuple6 = ('second',)
print(tuple5 + tuple6)
# 遍历元组tuple5，如果元素是list 遍历list
for x in tuple5:
    if isinstance(x, list):
        for y in x:
            print(y)
    else:
        print(x)

print(10 / 3)
print(10 // 3)
