"""
@desc smtp发送邮件，成功
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

qq_sender = "xxx@qq.com"
qq_pass = "xxxxxx"
qq_user = "xxx@qq.com"


def mail():
    ret = True
    try:
        msg = MIMEText("内容", "plain", "utf-8")
        msg["From"] = formataddr(["fromVeaba", qq_sender])  # 发件人昵称，发件人邮箱
        msg["To"] = formataddr(["QQuser", qq_user])  # 昵称，收件人邮箱
        msg["Subject"] = "Python 使用QQ SMTP"  # 主题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(qq_sender, qq_pass)
        server.sendmail(qq_sender, [qq_user, ], msg.as_string())
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print("发送成功")
else:
    print("发送失败")
