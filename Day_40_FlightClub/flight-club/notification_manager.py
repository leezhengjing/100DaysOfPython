from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["TWILIO_VIRTUAL_NUMBER"]
TWILIO_VERIFIED_NUMBER = os.environ["TWILIO_VERIFIED_NUMBER"]

MY_GMAIL = os.environ["MY_GMAIL"]
MY_YMAIL = os.environ["MY_YMAIL"]
GMAIL_PASSWORD = os.environ["GMAIL_PASSWORD"]
YAHOO_PASSWORD = os.environ["YAHOO_PASSWORD"]


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)

    def send_emails(self, address, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=GMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=address,
                msg=f"Subject:ZJ's Flight Club\n\n{message}",
            )
