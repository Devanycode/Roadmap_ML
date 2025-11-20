from twilio.rest import Client
from dotenv import load_dotenv
import os 

load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        # self.acount_sid = os.getenv("TWILIO_SID")
        # self.auth_token = os.getenv("AUTH_TOKEN")
        pass

    def send_sms(self, message):
        client = Client(self.acount_sid, self.auth_token)

        message = client.messages.create(
            body=message,
            from_="+13612668748",
            to="+573023660773",
        ) 

        print(message.body)