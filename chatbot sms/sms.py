from twilio.rest import Client

account_sid = 'AC2c0fa144182399e3f5fa082ad3da16ec'
auth_token = '54aaa1d73be651081171a1df45f7f95f'
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    client.messages.create(
        to=to_number,
        from_='+15739430564',
        body=message
    )


# Usage
to_number = '+919121525359'
sms_message = 'Hello, this is a test SMS from your app.'
send_sms(to_number, sms_message)
