#! /usr/bin/env python3
# coding = utf-8

import os
from time import strftime, gmtime
import smtplib
import mimetypes
from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from collections import namedtuple

# who want to send?
date1 = strftime('%Y%m%d', gmtime())
send_time = str(time.time())

mailto_list = ['chiyxme@outlook.com']
subject = (date1 + "_" + "SearchDownRight")
content = "the test content"

# the sender info
EmailSender = namedtuple('EmailSender', 'host,user,password,port')
email_account = 'chiyxme@gmail.com'
print('Please Enter your email({0}) password:'.format(email_account))
password = input()
sender = EmailSender(
    host='smtp.gmail.com',
    user=email_account,
    password=password,
    port=465
)


def send_email(to_list, sub, content):
    '''
    to_list: who to send
    sub: subject
    content: email content
    '''
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = sender.user
    msg['To'] = ';'.join(to_list)
    # attach content
    txt = MIMEText(content)
    msg.attach(txt)

    # send
    try:
        s = smtplib.SMTP_SSL()
        s.connect(sender.host, sender.port)
        # login
        s.ehlo()
        s.login(sender.user, sender.password)
        s.sendmail(sender.user, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    if send_email(mailto_list, subject, content):
        print('send success')
    else:
        print('send failure')
