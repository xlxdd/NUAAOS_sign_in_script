import requests
import time
import winsound
from datetime import datetime

url = 'https://www.nuaalab.cn/os/upload/jobs.js'

#winsound.Beep(1500, 1000)  # 发出警告提示音

while True:
    response = requests.get(url)
    data = response.text
    data_after_comment = data.split('*/', 1)[-1]
    if 'txt' in data_after_comment:
        print('Found "txt" in data')
        winsound.Beep(1000, 500)  # 发出警告提示音
    else:
        print('"txt" not found in data',end = "")
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Current time:', current_time)
    time.sleep(10)
