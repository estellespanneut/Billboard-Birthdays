# app/email_service.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")


def send_email(subject="[Birthday and Songs] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
    """
    Sends an email with the specified subject and html contents to the specified recipient,
    If recipient is not specified, sends to the admin's sender address by default.
    """

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e.message)
        return None


if __name__ == "__main__":
    example_subject = "[Birthday and Songs] This is a test"

    example_html = """
    <img src="https://images-na.ssl-images-amazon.com/images/I/71uqL5rr8%2BL._AC_SL1500_.jpg" alt="Trulli" width="700" height="275">

    <h3 style="color:purple">This is a test of the Billboard Birthday service</h3>
    
    <h4>Today's Date</h4>
    <p>Monday, January 1, 2040</p>
    <h4>Billboard Songs</h4>
    <ul>
        <li>1. song 1 | artist 1%</li>
        <li>2. song 2 | artist 2</li>
        <li>3. song 3 | artist 3</li>
    </ul>

    <h5 style="background-color:Violet;" height="700"> </h5>

    """

    send_email(example_subject, example_html)