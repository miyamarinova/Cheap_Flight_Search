from twilio.rest import Client

TWILIO_ACCOUNT_SID = "AC8cc0f7e59903545250d78e940fb2de58"
TWILIO_TOKEN = "65f5d0144225336f8f70c5532dd672d2"
TWILIO_NUMBER = "+19804009361"
MY_NUMBER = "+12025107305"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )

        print(message.sid)