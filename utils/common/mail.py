import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, to_email):

    #user modeli yapıldıktan sonra bunlar veritabanından çekilecek
    admin_mail = 'online_shopping_app@outlook.com'
    admin_password = 'Online_shopping123'

    msg = MIMEText(message)
    msg['From'] = admin_mail
    msg['To'] = to_email
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(admin_mail, admin_password)
        server.sendmail(admin_mail, to_email, msg.as_string())
        server.quit()
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderilirken bir hata oluştu: {e}")

