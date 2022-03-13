# below is excample we can use After the scraping py program runs and save a txt file
# this program will create and send a mail msg with credential imported from the config file 
# the mail msg will insert the the contents of the txt file into the msg body. should be saved in the same directory 
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:39:45 2019

@author: bobtr
"""

import smtplib, ssl
import configHACK

# Import the email modules we'll need
from email.message import EmailMessage

#example values used below
def send_email(subject, msg):
    try:
        #mailserver = smtplib.SMTP('smtp.office365.com',587)
        mailserver = smtplib.SMTP('smtp.example.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(configHACK.EMAIL_ADDRESS, configHACK.PASSWORD)
        message = 'Subject: {}\n{}'.format(subject, msg)
        mailserver.sendmail(configHACK.EMAIL_ADDRESS, configHACK.RECIPIENTS, message)
        mailserver.quit()
        print("Success: Email Sent.")
    except:
        print("Email failed to send")
        
subject = "Hacker News - Ycombinator" 

# Open the plain text file whose name is in textfile for reading.
with open('HackerDaily.txt', encoding="utf8", errors='ignore') as f:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(f.read())
    msg['From'] = "admin@test"


send_email(subject, msg)
