import datetime
import os
from fastapi import Depends, HTTPException,status
from src.user.schema import schemas


from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ssl import create_default_context
from email.mime.text import MIMEText
from smtplib import SMTP
import logging
from src.user.schema.schemas import MailBody
from dotenv import load_dotenv


load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Utility to hash plain password
def hash_password(plain_password):
    return pwd_context.hash(plain_password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)





def send_mail(data: MailBody | None = None):
    HOST = os.getenv('MAIL_HOST')
    USERNAME = os.getenv('MAIL_USERNAME')
    PASSWORD = os.getenv('MAIL_PASSWORD')
    PORT = os.getenv('MAIL_PORT')
    print(PASSWORD)
    
    msg = data
    message = MIMEText(msg.body, "html")
    message["From"] = USERNAME
    message["To"] = msg.to
    message["Subject"] = msg.subject

    ctx = create_default_context()


    try:
        with SMTP(HOST, PORT) as server:
            server.ehlo()
            server.starttls(context=ctx)
            server.ehlo()
            server.login(USERNAME, PASSWORD)
            server.send_message(message)
            server.quit()
        return {"status": 200, "errors": None}
    except Exception as e:
        return {"status": 500, "errors": e}
    

