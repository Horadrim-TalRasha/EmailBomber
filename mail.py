import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from config import *


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


class EMail():
    def __init__(self):
        pass

    def send_email(self):
        pass

    def recv_email(self):
        pass


class EMailImpl(EMail):
    def __init__(self):
        EMail.__init__(self)

    def send_email(self, mail_config, mail_content, mail_subject):
        mail_server = smtplib.SMTP_SSL(mail_config.get_config_value("smtp_serv"), mail_config.get_config_value("port"))
        mail_server.login(mail_config.get_config_value("sender"),
                          mail_config.get_config_value("password"))

        sender = mail_config.get_config_value("sender")
        reciever = mail_config.get_config_value("reciever")

        msg = MIMEText(mail_content, "plain", "utf-8")
        msg['From'] = sender
        msg['To'] = reciever
        msg['Subject'] = mail_subject
        mail_server.sendmail(sender, [reciever], msg.as_string())
        mail_server.quit()


    def recv_email(self):
        print "receive email here"

if __name__ == "__main__":
    TXMail = EMailImpl()
    mail_config = JsonConfig("./mail.conf")
    mail_config.read_from_config_file()
    TXMail.send_email(mail_config, "green tea bitch", "new year present")
