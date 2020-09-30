# -*- encoding=utf8 -*-
__author__ = "Admin"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
import random
import requests
import json



def ini():
    time_d = time.time()
    x = str(time_d).replace('.','')[5:11]
    email = hex(int(x))
    lastNa = oct(int(x))
    return email,lastNa

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555",
    ])


# script content
print("start...")


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__) 

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



touch(Template(r"tpl1601189173337.png", record_pos=(0.169, 0.046), resolution=(1600, 900)))

time.sleep(random.random() *2+5)
touch(Template(r"tpl1600933681153.png", record_pos=(-0.001, 0.345), resolution=(1440, 2960)))
time.sleep(random.random())

def ini():
    time_d = time.time()
    x = str(time_d).replace('.','')[5:11]
    email = hex(int(x))
    lastNa = oct(int(x))
    return email,lastNa

def sign():
    email,lastNa = ini()
    input_email = poco(name='com.famousfootwear.android:id/auth_email_search')   #输入邮箱
    input_email.click()
    time.sleep(random.random())
    text(email+lastNa+"@htbh.club")      #输入邮箱
    time.sleep(random.random())
    touch(Template(r"tpl1601032459192.png", record_pos=(-0.002, 0.128), resolution=(810, 1440)))
    time.sleep(random.random())

    
    input_firstName = poco(name='com.famousfootwear.android:id/auth_first_name')  #firstNamesleep(1.0)

    input_firstName.click()
    time.sleep(random.random())
    text(email)      #输入firstName
    time.sleep(random.random() *2+1)
    
    
    input_lastName = poco(name='com.famousfootwear.android:id/auth_last_name',text='Last Name')  #lastName
    # input_lastName.click()
    time.sleep(random.random())
    text(lastNa)      #输入firstName
    time.sleep(random.random())

    
    btn_continue = poco(name='com.famousfootwear.android:id/auth_create_continue')  #点击注册按钮
    # btn_continue.click()
    time.sleep(random.random() *2+1)


    input_pwd = poco(name='com.famousfootwear.android:id/auth_password',text='Enter Your Password')  #password
    input_pwd.click()
    time.sleep(random.random())
    text(email)
    time.sleep(random.random())
    btn_finish = poco(name='com.famousfootwear.android:id/auth_create_password_continue') #点击密码设置 完成
    # btn_continue.click()
    time.sleep(random.random() *2+1)

    btn_account = poco(name='com.famousfootwear.android:id/bottom_nav_image',desc='Account')  #点击Account
    btn_account.click()
    time.sleep(random.random() *2+1)
    btn_sign_out = poco(name='com.famousfootwear.android:id/account_navigation_sign_out',type='android.widget.Button')   #退出账号
    btn_sign_out.click()
    time.sleep(random.random() *2+4)


    new_btn_sign = poco(name='com.famousfootwear.android:id/guest_authenticate')  #新注册元素
    time.sleep(random.random() *2+1)
    new_btn_sign.click() #新注册点击
    
def start():
    json_text = {
        "msgtype": "text",   #消息类型
        "text": {
            "content": text_start,   #文本内容
            "mentioned_list":["wangshifeng"],    #userid列表 @某个成员
            "mentioned_mobile_list": begin       #手机号列表  @某个成员
        }
    }   #开始发送消息
    print(json_text)
    print(requests.post(api_url, json.dumps(json_text), headers=headers, verify=False).content)

    
def stop():
    json_text = {
        "msgtype": "text",  # 消息类型
        "text": {
            "content": text_stop,  # 文本内容
            "mentioned_list": ["wangshifeng"],  # userid列表 @某个成员
            "mentioned_mobile_list": begin      # 手机号列表  @某个成员
        }
    }   #结束发送消息
    print(json_text)
    print(requests.post(api_url, json.dumps(json_text), headers=headers, verify=False).content)

    
def error():
    json_text = {
        "msgtype": "text",  # 消息类型
        "text": {
            "content": text_error,  # 文本内容
            "mentioned_list": ["wangdefa"],     # userid列表 @某个成员
            "mentioned_mobile_list": bug        # 手机号列表  @某个成员
        }
    }   #bug消息
    print(json_text)
    print(requests.post(api_url, json.dumps(json_text), headers=headers, verify=False).content)

    
if __name__ == '__main__':
    
    key = "d17d6e04-b241-4e28-b6a6-5020bf8942bc"
    api_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s" % key

    text_start = '开始注册账号啦'
    text_stop = '账号已注册完成啦'
    text_error = '程序出现bug啦'

    begin = ['15538403012']
    bug = ['15836321705']

    headers = {'Content-Type': 'application/json;charset=utf-8'}
#     start()
#     time.sleep(3)
#     stop()
#     time.sleep(4)
#     error()
    
    
    start()
    try:
        for i in range(200):
            print('正在注册第{}个账号'.format(i+1))
            sign()
            print('已经成功注册{}个账号'.format(i+1))
    except Exception as e:
        error()
        exit()
    stop()
    

