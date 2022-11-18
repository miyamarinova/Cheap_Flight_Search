
from twilio.rest import Client
import smtplib

TWILIO_ACCOUNT_SID = "AC8cc0f7e59903545250d78e940fb2de58"
TWILIO_TOKEN = "19042617231a6c911c9144a0a16e1ee2"
TWILIO_NUMBER = "+19804009361"
MY_NUMBER = "+12025107305"

MAIL_PROVIDER_SMTP_ADRESS = "smtp.gmail.com"
MY_EMAIL = "mariayoana.marinova@gmail.com"
MY_PASSWORD = "tmahgoyljurllnao"

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

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,msg=f"Subject:NEW LOW PRICE FLIGHT!\n\n{message}\n".encode("utf-8"))