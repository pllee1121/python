from wxpy import *
import requests
import json

# sinfriendlist = []
friendname = input('请输入你要自动回复的人的备注：')
# sinfriendlist.append(friendname)
# with open('friend.txt','r',encoding='utf-8') as f,open('friend.txt','w',encoding='utf-8') as f1:
#     for line in f:
#         data = line.split('')

bot = Bot(cache_path=True)
myfriend = bot.search('%s' % friendname)[0]


# myfriend1 = bot.search('李钢')[0]
# sister = bot.search('姐')[0]
# friend = bot.search('王传林')[0]
# myfriend2 = bot.search('刘清政老师')[0]


def auto_reply(text):
    url = 'http://www.tuling123.com/openapi/api'
    api_key = 'f66b3909927f4c83b3a7d63be236782f'
    send_dic = {
        'key': api_key,
        'info': text
    }
    # 把python中的字典，转换成json格式字符串
    send_str = json.dumps(send_dic)
    response = requests.post(url, data=send_str)
    response_dic = json.loads(response.text)
    return response_dic['text']


@bot.register()
def recv_send_msg(recv_msg):
    print(recv_msg.text)
    if recv_msg.sender == myfriend:  # or recv_msg.sender == myfriend1 or recv_msg.sender == sister or recv_msg.sender == friend:
        # 通过好友发送过来的文字，自动生成回复信息
        back_text = auto_reply(recv_msg.text)
        return back_text


embed()

# from wxpy import *
# import requests
# import json
#
# bot = Bot(cache_path=True)
# group = bot.groups().search('宿州学院Python实训')[0]
# my_friend = group.search('刘sir')[0]
#
#
# def auto_reply(text):
#     url = 'http://www.tuling123.com/openapi/api'
#     api_key = '9df516a74fc443769b233b01e8536a42'
#     send_dic = {
#         'key': api_key,
#         'info': text
#     }
#     # 把python中的字典，转换成json格式字符串
#     send_str = json.dumps(send_dic)
#     response = requests.post(url, data=send_str)
#     response_dic = json.loads(response.text)
#     # {
#     #     "code": 100000,
#     #     "text": "嘿嘿，你好我好，大家都好~"
#     # }
#     return '【来自智能机器人：】' + response_dic['text']
#     # 把json格式字符串，转换成python中的字典
#     # json.loads()
#
#
# @bot.register(chats=group)
# def recv_send_msg(recv_msg):
#     print(recv_msg.text)
#     if recv_msg.member == my_friend:
#         # 通过好友发送过来的文字，自动生成回复信息
#         back_text = auto_reply(recv_msg.text)
#         return back_text
#
#
# embed()
