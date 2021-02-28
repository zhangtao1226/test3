# -*- coding = urf-8 -*-
# @Time : 2021/1/10 下午1:15
# @Author : ZhangTao
# @File : test_email.py
# @Software : PyCharm

import smtplib

sm = smtplib.SMTP()
sm.connect('smtp.qq.com', '25')  #建立连接
aa = sm.login('826517451@qq.com','zhangtao122630')  #登陆账户
print(aa)
# sm.sendmail('邮件发送方','邮件接受方','邮件内容') #发送邮件
# sm.quit() #关闭连接，结束邮件服务