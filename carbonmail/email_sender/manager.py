# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar este pacote (gerenciador)

from carbonmail.carbon.manager import download_image
import os
import ssl
import smtplib
import threading

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from decouple import AutoConfig

from carbonmail.list_editor.manager import get_list_contacts
from carbonmail.utils import root_folder, string_null_or_empty


def initialize():
    from carbonmail.email_sender import Email_Sender

    ems = Email_Sender()
    ems.enable_window()


def validate_email_sending(window, title, content, code_path, list_name):
    contacts = get_list_contacts(list_name)

    if not contacts or len(contacts) == 0:
        return 0

    if string_null_or_empty(title) or string_null_or_empty(content):
        return -1

    if not os.path.isfile(code_path):
        return -2

    threading.Thread(
        target=send_mass_email, args=(window, contacts, title, content, code_path)
    ).start()

    return 1


def send_mass_email(window, contacts, title, content, code_path):
    image_path = download_image(code_path)

    for contact in contacts:
        send_email(contact, title, content, image_path)

    window.write_event_value("-Sent-", "Done")


def send_email(contact, title, content, image_path):
    config = AutoConfig(search_path=root_folder())

    SMTP_USER = config("SMTP_USER")
    SMTP_PASSWORD = config("SMTP_PASSWORD")
    SMTP_SERVER = config("SMTP_SERVER")
    SMTP_PORT = config("SMTP_PORT")

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    message = MIMEMultipart()
    message["Subject"] = title
    message["From"] = SMTP_USER
    message["To"] = f"{contact[0]} <{contact[1]}>"

    body = MIMEText(content.replace("#NOME#", contact[0]))
    message.attach(body)

    image = MIMEImage(image_data, name=os.path.basename(image_path))
    message.attach(image)

    context = ssl.create_default_context()

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, contact, message.as_string())

    print(f"Enviou e-mail para: {contact[0]} <{contact[1]}>")
