from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
import requests
import winsound
from datetime import datetime

#文件名称
fname = "roll-0528.txt"
#文件绝对路径
fpath = r"C:\Users\xlxdd\Desktop\PY\{}".format(fname)
#fpath = r'C:\Users\xlxdd\Desktop\OS\sfind.c'

def listen():
    url = 'https://www.nuaalab.cn/os/upload/jobs.js'
    #开始监听网页
    while True:
        response = requests.get(url)
        data = response.text
        data_after_comment = data.split('*/', 1)[-1]
        #if True:
        if 'txt' in data_after_comment:
            #监听到出现txt
            print('Found "txt" in data')
            winsound.Beep(1000, 500)  # 发出警告提示音
            upload()
            exit()
        else:
            #否则打印时间信息
            print('"txt" not found in data',end = "")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('Current time:', current_time)
        #时间间隔设置为十秒
        time.sleep(10)


def upload():
    # 使用谷歌浏览器
    driver = webdriver.Chrome()
    # 用cookies打开并登陆网页
    with open('cookies.pkl', 'rb') as f:
        cookies = pickle.load(f)
    driver.get("https://www.nuaalab.cn/os/upload/")
    time.sleep(1)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(1)

    #创建本地文件
    with open(fname, 'w') as f:
        pass
    # 找到上传文件按钮的 HTML 元素
    uploads = driver.find_elements(By.XPATH,"//input[@type='file']")
    file_input = uploads[1]
    # 输入本地文件的路径
    file_input.send_keys(fpath)
    time.sleep(3)
    # 找到按钮的 HTML 元素
    buttons = driver.find_elements(By.XPATH,"//input[@type='button'][@value='上传']")
    upload_button = buttons[1]
    #点击按钮
    driver.execute_script("arguments[0].click();", upload_button)
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    listen()