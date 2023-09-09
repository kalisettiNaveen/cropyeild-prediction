from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

chatbot = ChatBot('MyBot')
# Train the chatbot if needed

account_sid = 'AC2c0fa144182399e3f5fa082ad3da16ec'
auth_token = '54aaa1d73be651081171a1df45f7f95f'
client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = chatbot.get_response(user_input)
    return str(response)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    to_number = request.form['to_number']
    sms_message = request.form['sms_message']
    client.messages.create(
        to=to_number,
        from_='your_twilio_number',
        body=sms_message
    )
    return 'SMS sent successfully.'

@app.route('/send_email', methods=['POST'])
def send_email():
    subject = request.form['email_subject']
    message = request.form['email_message']
    recipient_email = request.form['recipient_email']
    
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    
    return 'Email sent successfully.'

if __name__ == '__main__':
    app.run(debug=True)
