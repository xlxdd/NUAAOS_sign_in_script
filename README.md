# NUAAOS_sign_in_script
## NUAA操作系统实验课自动签到脚本  
***  
### 简单监听功能  
alert.py可以实现对`https://www.nuaalab.cn/os/upload/jobs.js`内容的监听，当出现"txt"时表示出现了签到内容，系统会发出蜂鸣声  
### 自动签到功能  
#### 准备  
首先需要自行安装自动化测试工具chromedriver，并且添加可执行文件目录到系统路径PATH 
#### 操作步骤
实现自动签到，需要先运行createcookie.py手动登陆网页创建cookie  
然后运行listen.py  
需要手动修改fname和fpath的内容设置文件名和绝对路径 
***
### 备注  
写的比较简陋，并没有很智能。提供了一个思路，后续课根据需要自行修改。 
这个脚本现在可能已经没有什么用处了，但我了解到了不少自动化测试相关知识，哈哈
