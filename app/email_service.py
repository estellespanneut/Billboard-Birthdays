# app/email_service.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

TEMPLATE_ID = "d-05507d891d5b41248bf693b643ec804d"

def SendDynamic():
    """ Send a dynamic email to a list of email addresses

    :returns API response code
    :raises Exception e: raises an exception """
    # create Mail object and populate
    message = Mail(
        from_email=SENDER_EMAIL_ADDRESS,
        to_emails=SENDER_EMAIL_ADDRESS)
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'subject': 'Billboard Chart on Your Birthday!',
    }
    message.template_id = TEMPLATE_ID
    # create our sendgrid client object, pass it our key, then send and return our response objects
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        print("Response code:", code)
        print("Response headers:", headers)
        print("Response body:", body)
        print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))
    return str(response.status_code)


if __name__ == "__main__":
    SendDynamic()