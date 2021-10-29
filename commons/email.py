from django.core.mail import send_mail
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def email(subject, message, to, html_message=None):
    send_mail(
        subject, 
        message, 
        "Soporte<davidarellanocii@gmail.com>",
        [to],
        fail_silently=False,
        html_message= html_message
    )