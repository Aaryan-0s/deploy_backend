import random

from fastapi import HTTPException

from src.user.schema.schemas import MailBody
from src.user.utils.utils import send_mail
from src.user.model.models import VerificationCode, User
from src.user.repository.repository import VerificationRepo



def send_verification_email(user:User, code:int):    
    try:
        to = user.email
        subject = "Email Verification"
        body = f"Use the following code to verify your email {code}"
        mail_body = MailBody(to=to, subject=subject, body=body)
        resp = send_mail(mail_body)
        return resp
    
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error sending verification email : {e} ")
    

def send_reset_password_email(user:User, code:int):    
    try:
        to = user.email
        subject = "Reset password"
        body = f"Use the following code to reset your password {code}"
        mail_body = MailBody(to=to, subject=subject, body=body)
        resp = send_mail(mail_body)
        return resp
    
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error sending verification email : {e} ")