count = 1
sum = 0
while count <= 100:
    sum = sum + count
    count = count + 1
    print(sum)
print(sum)

count = 1
sum = 0
while count <= 100:
    sum = sum + count
    count = count + 1
    if sum > 1000:
        break
print(sum)

count = 1
sum = 0
while count <= 100:
    if count % 2 == 0:
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print(sum)

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

print('--------for循环')
tuple1 = ('a', 'b', 'c', 1, 2, 3)
for x in tuple1:
    print(x)

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
   for i in range(2, num):  # 根据因子迭代
      if num % i == 0:      # 确定第一个因子
         j = num/i          # 计算第二个因子
         print ('%d 是一个合数' % num)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print('%d 是一个质数' % num)
