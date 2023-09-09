import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, recipient_email):
    sender_email = 'naveenkalisetti123@gmail.com'
    sender_password = '6302664408'
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Usage
email_subject = 'Important Notification'
email_message = 'This is an important notification from your app.'
recipient_email = 'gsumanth101@gmail.com'
send_email(email_subject, email_message, recipient_email)
