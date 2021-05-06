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

               """
Hello , %s
    Here is your OTP for e-mail verification : %s
Let your keys fly your imagination,
Regards , Blogarithm team.
               """
              ]
mail['reset password'] = ['OTP for Password Reset',
                          """
Hello , %s
    Here is your OTP to reset your password : %s
Let your keys fly your imagination,
Regards , Blogarithm team.
                          """
                         ]

mail['admin email'] = ['Mail from admin@Blogarithm',
                       """
Hello , %s
    It has come to our attention that your blog titled: %s
    contains abusive contents that voilate our terms.
    Kindly rearrange it within 7 days or we will be forced
    to delete your blog from our platform.
NO FURTHER NOTICE WILL BE PROVIDED
Regards , Blogarithm team.
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
    
    if email_type=="admin email":
        content = mail[email_type][1] %(rec , other['title'])
    else:
        content = mail[email_type][1] %(rec , other['otp'])

    mail_content = MIMEText(content, 'plain')
    
    msg.attach(mail_content)

    #Send Mail
    smtp.sendmail(EMAIL_ID, rec , msg.as_string())

    print(f"Mail sent to {rec}")

    smtp.quit()
