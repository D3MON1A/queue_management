# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

def send(body='Some body', to=''):
    
    account_sid = os.getenv("sid")
    auth_token = os.getenv("token")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="body",
                        from_='+12058096948',
                        to='+1'
                    )

    print(message.sid)
send()