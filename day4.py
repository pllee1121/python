# 元组  只能取值
# ages = ('lll', 0, [1, 2, 3])
# print(ages)
# print('lll' in ages)
# print()
# print(len(ages))
# for i in ages:
#     print(i)
# info = {'apple': 'hello', 'organ': 'bye'}
'''
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
'''
# info={
# 'apple':10,
# 'tesla':100000,
# 'mac':9000,
# 'lenovo':3000,
# 'chicken':10,
# }
# for key in info:
#         print('商品名: %s 商品价格: %s' % (key, info[key]))
# shoppingcart = []
# while True:
#     name = input('请输入商品名:').strip()
#     if name == 'q':
#         for goods in shoppingcart:
#             print('''商品名: %s 商品价格: %s 商品数量: %s''' % (goods[0], goods[1], goods[2]))
#         break
#     if name not in info:
#         continue
#     count = input('请输入商品数量:').strip()
#     if count.isdigit():
#         count = int(count)
#     shoppingcart.append([name, info[name]*count, count])    #每一个
#     ll = shoppingcart[-1]
#     print('''以把商品名: %s商品价格: %s商品数量: %s到购物车''' % (ll[0], ll[1], ll[2]))
    # print('''商品名: %s商品价格: %s商品数量: %s''' % (shoppingcart[0][0], shoppingcart[0][1], shoppingcart[0][2]))
    # break


# dic = {'name':'pllee','age':20,'sex':'male'}
# dic['hobby'] = '剪发'
# print(dic)
# print(len(dic))
# print('hobby' in dic)
# dic.pop('hobby')
# print(dic)
# dic.popitem()   #随机移除
# print(dic)
# print(dic.keys())   #取key值
# print(list(dic.keys()))
# print(list(dic.values()))
# print(list(dic.popitem()))



# 打印key值
# print('第一种方法打印key值')
# for key in dic:
#     print(key)
# print('第二种方法打印key值')
# for key in dic.keys():
#     print(key)
# print('-----')
# # 第一种方法打印value值
# print('第一种方法打印value值')
# for value in dic.values():
#     print(value)
# #     第二种方法打印value值
# print('第二种方法打印value值')
# for key, value in dic.items():      #生成元组
#     print('key: %s   value: %s'% (key, value))


# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
#
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# number = [11,22,33,44,55,66,77,88,99,90]
# key1 = {}
# key2 = {}
# value1 = '大于66的数'
# value2 = '小于66的数'
# for i in number:
#     if i > 66:
#         key1[i] = i
#     else:
#         key2[i] = i
# print(key1)
# print(key2)

# dic = {'k1':[], 'k2':[]}
# ll = [11,22,33,44,55,66,77,88,99,90]
# for i in ll:
#     if i > 66:
#         dic['k1'].append(i)
#     elif i < 66:
#         dic['k2'].append(i)
# print(dic)


# 统计s='hello alex alex say hello sb sb'中每个单词的个数
# s = 'hello alex alex say hello sb sb'
# dic = {}
# ll = s.split()    #切分
# for word in ll:
#     if word in dic:
#         dic[word] += 1
#     else:
#         dic[word] = 1
# print(dic)

# 字典关键字不能重复
# 可变类型 列表 字典
# 不可变类型 数字 字符串 元组
# dic = {'hello':6, 'hello':1}
# print(dic)
# # 字典get方法，可以设置默认值，当key不存在时，返回默认值
# dic = {'hello':6,'sb':1}
# print(dic['sb'])
# print(dic['dsb'])
# print(dic.get('dsb','这个值不存在'))

#
# ll = [1,2,3,4]
# print(id(ll))
# ll.append(5)
# ll.pop(0)
# print(id(ll))
#
#
#
# pythons = {'alex','egon','yuanhao','ligang','lipengliang','wangzhidong'}
# linux = {'ligang','lipengliang','wangzhidong','ale'}
# print(pythons&linux)
# print(pythons | linux)



# f = open('a.txt','r')
# date = f.read()
# print(date)
# f.close()

# with open('a.txt', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print(data)
#     print(id(f))
#     print(type(f))
# with open('a.txt','w',encoding='utf-8') as f:   #回清空a.txt
#     f.write('pllee')
# with open('a.txt','a',encoding='utf-8') as f:
#     f.write(' love you')
# with open('a.txt','wt',encoding='utf-8') as f:
#     f.write(' love you')

# 二进制
# with open('a.txt','rb') as f:
#     print(f.read())

# 可读可写
# with open('a.txt','r+') as f:
#     print(f.readable())
#     print(f.writable())


source = input('请输入要拷贝的文件')
copy = input('请输入要拷贝成的文件')
with open(source, 'rb') as f, open(copy, 'wb') as f2:
    data = f.read()
    f2.write(data)
