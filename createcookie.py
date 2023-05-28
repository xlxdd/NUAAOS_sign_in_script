from selenium import webdriver
import pickle
#使用谷歌浏览器
driver = webdriver.Chrome()

# 手动登录网页
input('请手动登录网页，然后按回车键继续...')

# 获取登录后的cookies
cookies = driver.get_cookies()

with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

driver.close()