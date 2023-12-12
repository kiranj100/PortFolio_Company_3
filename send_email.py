import smtplib
import ssl

def send_email(message):
    server = "smtp.gmail.com"
    ssl_port = 465
    me_user = "kiranjojan455@gmail.com"
    my_password = "eyfeuoilqhspbxgd"

    receiver = me_user

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(server,ssl_port,context=my_context) as server:
        server.login(me_user,my_password)
        server.sendmail(me_user,receiver,message)

