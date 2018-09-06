# name = 'pllee'
# print(id(name),type(name),name)
#
# age = 19
# print(id(age))
# print(type(age))
# print(age)
# name = input('please input:\t')
# print(name)
# '''
# 你好 我现在正在进行注释
#
# '''
#
# explain = '''hello'''
# print(explain)
# msg = '''
# 今天我想写首小诗，
# 歌颂我的同桌，
# 你看他那乌黑的短发，
# 好像一只炸毛鸡。
# '''
# print(msg)
# li = ['李刚', '李朋亮', '王之洞', '顾凯阳', 18, ['沙雕', '傻逼']]
# print(li[5])
# print(type(li[5]))
# print(li[5][0])
# student_info = [['ligang', 18, ['play', 'sleep']], [18,90]]
# print(student_info[0])
# '''
# # pir
#
# #  字典  key:value
# #
# # '''
# students = {'ligang': 18, 'lipengliang': 20}
# print(students['ligang'])
# info = {
#     'name': 'egon',
#     'hobbies': ['play', 'sleep'],
#     'company_info': {
#         'type': 'education',
#         'name': 'Oldboy',
#         'emp_num': 40,
#     }
# }
# print(info['company_info']['name']) #取公司名
#
#
# students=[
#     {'name':'alex','age':38,'hobbies':['play','sleep']},
#     {'name':'egon','age':18,'hobbies':['read','sleep']},
#     {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
# ]
# print(students[1]['hobbies'][1]) #取第二个学生的第二个爱好
#
# student = {'zhangsan': [18, {'sex': 'male'}, ['play', 'read', 'sleep']],
#            'lisi': [28, {'sex': 'female'}, ['play', 'sleep']],
#            'wangwu': [88, {'sex': 'female'}, ['play', 'sleep', 'game']],
#            }
#
# print(student['zhangsan'][1]['sex'])
# print(student['wangwu'][2][1])
# print(student['lisi'][0])
#
# name= ''
# if name:
#     print('True')
# else:
#     print('False')
# name = 'OK'
# if name:
#     print('True')
# else:
#     print('False')
#
# name = input('please input name:\t')
#
# age = input('please input age:\t')
#
# job = input('please input job:\t')
#
# print('------------ information -----------')
#
# print('name :\t'+name)
#
# print('age  :\t'+age)
#
# print('job  :\t'+job)
#
# print('------------- end -----------------')
#
# digtal = 10.5*40.0
# digtal1 = 8*2
# digtal2 = digtal/digtal1
# print(digtal2)
#
# print(True or Flase and False)
#
# age = 19
# if age > 30:
#     print('阿姨')
# else:
#     print('小姐姐')
#
# age = 40
# height = 170
# weight = 90
# is_pretty = True
# success = False
# if age >= 18 and height >= 170 and weight <= 100 and is_pretty is True:
#     success = True
#     print('表白')
#     if success:
#         print('在一起，很高兴')
#     else:
#         print('爱情不存在的')
# else:
#     print('阿姨')
#
# score=input('>>: ')
# score=int(score)
#
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 70:
#     print('普通')
# else:
#     print('很差')
# age = 18
# # accout = 0
# while True:
#     # accout += 1
#     guess = input('please input a number :\n')
#     guess = int(guess)
#     if guess > age:
#         print('猜大了')
#     elif guess < age:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#
# for i in range(10):
#         print('%s*%s=%s'%(i,j,i*j),end='    ')
#     print(i)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#     print()
# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)
for i in range(1, 101, 2):
    print(i, end=' ')
print()

max_level = 5
for current_level in range(1, max_level + 1):
    for i in range(max_level - current_level):
        print(' ', end='')  # 在一行中连续打印多个空格
    for j in range(2 * current_level - 1):
        print('*', end='')  # 在一行中连续打印 * 号
    print()
