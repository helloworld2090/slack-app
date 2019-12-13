import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import hashlib
from GLOBAL import (GLOBAL_DATA , User, generate_token, 
generate_user_id)

def auth_password_reset_req(user_email):
    
    valid_email = False
    for users in GLOBAL_DATA["users"]:
        if user_email == users.email:
            valid_email = True
            break
    
    if valid_email == False:
        raise ValueError("email is not in our system")

    code = hashlib.sha256(user_email.encode()).hexdigest()
    #my email deets:
    email = 'bob.ma000@gmail.com'
    password = 'Polik91$'

    msg = MIMEMultipart()

    msg['From'] = email
    msg['To'] = user_email
    msg['Subject'] = 'password reset'

    msg.attach(MIMEText(code, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, user_email, code)
    server.quit()

    return {}