#! /usr/bin/env python3
# coding = utf-8

import smtplib
import imapclient

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# 链接&login
print("Please Enter password:")
password = input()
email = 'chiyxme@gmial.com'
print(imapObj.login(email, password))



