max_level = 5
for current_level in range(1,max_level+1):
    for i in range(max_level-current_level):
        print(' ', end='') #在一行中连续打印多个空格
    for j in range(2*current_level-1):
        print('*', end='')
    print()

count = 1
total = 0
while count < 100:
    if count % 2 ==0:
        total -= count
    else:
        total += count
    count += 1
print(total)
count = 1
while count<3:
    name = input('name:')
    password = input('password:')
    if name=='pllee' and password=='123':
        print('登陆成功')
        print('登陆了%s次'%count)
        break
    else:
        print('登陆失败')
        count+=1
motorcycles = ['yamaha', 'honda', 'suzuki']
print(motorcycles[0])
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)
total = 0
for count in range(100):
    if count % 2 == 0:
        total -= count
    else:
        total+=count
    count += 1
print(total)
sum = 0
count = 1
while count <101:
    sum += count
    count+= 1
print(sum)

sum = 0
for count in range(1, 101):
    sum += count
print(sum)
for i in range(10):
    print(i)
    # if i==8:
    #     break
else:
    print('正常执行')

ss = 'abcdefg'
print(ss[1:5:2])
print(len(ss))
print(('bcd' in ss))
bb = '   abcdefghijklmn  '
print(bb.strip())
print(bb[-2])
print(bb[2:5])
print(bb[2:9:3])
print('abb' in bb)
print(len(bb))
print(bb)
print(bb.strip())
''' 切分  '''
cc = 'pllee|20|170'
ll=cc.split('|')
print(type(ll))
print(ll)

dd = "pllee|ligang|wangzhidong|gukaiyang"
ee = dd.split('|')
print(type(ee))
print(ee)
for i in dd:
    print(i)

ss = 'pllleeligang'
count = 0
while count < len(ss):
    print(ss[count])
    count += 1

ss = 'pllleeligang'
for i in ss:
    print(i)


ss = '@   abcdefg  @'
print(ss.rstrip('@'))

print(ss.lstrip('@'))

print(ss.strip('@'))

print(ss.lower())
print(ss.upper())

ss = 'abcdefg'
print(ss.startswith('abc'))
print(ss.endswith('efg'))

'''

类似%占位符的其他用法

'''
print('my name is %s ,my ageis %s' %('pllee',20))
print('my name is {}, my age is {}'.format('pllee',20))
print("my name is {name}, my age is {age}".format(age = 20 , name = 'pllee'))
print('my name is {0}, my age is {1}, my name is {2}'.format('pllee', 20, 'qudeshun'))

aa = 'pllee|20|170'
ll = aa.split('|')
print(ll)
ll = aa.split('|', 1)
print(ll)
ll = aa.rsplit('|', 1)
print(ll)
bb = '*hello*world*'
print(bb.split('*'))
字符串拼接
ll = ['pllee', 'handsome']
print('|'.join(ll))

取代
ss = 'pllee is handsome man'
print(ss)
dd = ss.replace('handsome', 'beautiful')
print(dd)

ss = '1024'
print(ss.isdigit())

age = input('age:')
if age.isdigit():
    print(age)
else:
    print('您输入的字符含有不合规定字符，请输入数字')

my_girl_friends = ['pllee', 'ligang', 'wangzhidong', 4, 5]
print(my_girl_friends)
my_girl_friends[0] = 'liming'
print(my_girl_friends)
print(my_girl_friends[0:2])
print(my_girl_friends[0:5:2])
print(len(my_girl_friends))
print('liming' in my_girl_friends)
my_girl_friends.append('lipengliang')
print(my_girl_friends)
del my_girl_friends[0]
print(my_girl_friends)

my_girl_friends = ['pllee', 'ligang', 'wangzhidong', 4, 5]
my_girl_friends.remove('pllee')
print(my_girl_friends)
print(my_girl_friends)
print(my_girl_friends.pop())

my_girl_friends = ['pllee', 'ligang', 'wangzhidong', 4, 5]
# 方法一
count = 0
while count < len(my_girl_friends):
    print(my_girl_friends[count])
    count += 1
# 方法二
for girl in my_girl_friends:
    print(girl)
# 方法三
for girl in range(0, len(my_girl_friends)):
    print(my_girl_friends[girl])

删除操作
my_girl_friends = ['pllee', 'ligang', 'wangzhidong', 4, 5]
# 方法一
del my_girl_friends[0]
print(my_girl_friends)
# 方法二
my_girl_friends.pop()
print(my_girl_friends)
# 方法三
my_girl_friends.remove('wangzhidong')
print(my_girl_friends)

切片
my_girl_friends = ['pllee', 'ligang', 'wangzhidong', 4, 5]
print(len(my_girl_friends))
# 切片
girl = my_girl_friends[0:5:2]
print(girl)
# 追加
my_girl_friends.append('hello')
print(my_girl_friends)
# 成员运算,看是否在列表汇中
print('pllee'in my_girl_friends)

正向反向步长
l = [1, 2, 3, 4, 5, 6]
print(l[::-1])
print(l[0:3:1])
print(l[2::-1])

data = ['alex',49,[1996,8,15]]
a = data[0]
b = data[1]
c = data[2][0]
d = data[2][1]
e = data[2][2]
print(a, b, c, d, e)

index = []
index.append('1')
index.append('2')
index.append('3')
index.append('4')
print(index[-1])
print(index[-2])
print(index[-3])
print()
print(index.pop(0))
print(index.pop(0))
print(index.pop(0))
print(index.pop(0))

for i in range(5):
    i = input('please input:\t')
    index.append(i)
count = len(index)
for j in range(count):
    print(index.pop(0))
