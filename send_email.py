import smtplib
import email.message


from_email = input("Digite seu email:")
destiny_email = input("Digite o email de quem vai receber:")
subject = input("Digite o assunto do email:")
content = input("Digite a mensagem do email em forma de texto ou html:")
app_password = input("Digite a sua senha de app:")


def send_email():
    email_body = f"{content}"

    msg = email.message.Message()
    msg['Subject'] = f"{subject}"
    msg['From'] = f"{from_email}"
    msg['To'] = f"{destiny_email}"
    password = f'{app_password}'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


send_email()
