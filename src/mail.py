"""
Sending Mails
"""

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from os import environ

EMAIL_ID, EMAIL_PWD = environ['EMAIL'].split()

mail = dict()
mail['otp'] = ['OTP for Email Verification',
               f"""

               """
              ]
mail['reset password'] = ['OTP for Password Reset',
                          f"""

                          """
                         ]

mail['admin email'] = ['Mail from Admin@Blogarithm',
                       f"""

                       """
                      ]


def send_email(email_type, rec, **other):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail[email_type][0]
    msg['From'] = EMAIL_ID

    smtp = SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    #Login to email services
    smtp.login(EMAIL_ID, EMAIL_PWD)

    msg['To'] = rec
    
    mail_content = MIMEText(mail[email_type][1], 'plain')
    
    msg.attach(mail_content)

    #Send Mail
    smtp.sendmail(EMAIL_ID, rec , msg.as_string())

    print("Mail sent to %s" %rec)

    smtp.quit()
