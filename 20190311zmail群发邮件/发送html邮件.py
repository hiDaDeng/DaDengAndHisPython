import zmail

mail = {
    'subject': None,
    'content_text': None,
    'attachments': None,
}

mail['subject']='大邓的新课通知'
mail['content_html'] = open('模板.html').read()
mail['attachments'] = 'python文本分析.jpg'

#注意第一是发件的邮箱地址
#第二个参数是开启POP3/SMTP服务后的密码
server = zmail.server('auto_python@126.com', 'autopython123')

server.send_mail('thunderhit@qq.com', mail)
print('发送完成')

