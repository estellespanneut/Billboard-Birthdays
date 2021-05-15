import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime
from app import APP_ENV
import billboard #added
import json #added
import ast

# .env file should have SENDGRID_API_KEY and SENDER_EMAIL_ADDRESS variables
load_dotenv()

#
# user input
#

BIRTH_DATE = os.getenv("BIRTH_DATE", default="2000-01-01")
CHART_TYPE = os.getenv("CHART_TYPE", default="hot-100")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
TEMPLATE_ID = "d-05507d891d5b41248bf693b643ec804d" #sendgrid email template

def set_birth_date():
    if APP_ENV == "development":
        birth_date = input("""
            Please enter your birth date in YYYY-MM-DD format.
            For example, if your birth date is April 5th, 2000, enter '2000-04-05.'
            """)
    else:
        birth_date = BIRTH_DATE
    return birth_date

def set_chart_type():
    if APP_ENV == "development":
        chart_type = input("""
            Please enter the desired Billboard chart type to retrieve data from.
            Some charts available include 'hot-100', 'country-songs', 'pop-songs', 'r-b-hip-hop-songs.'
            If you want to view an entire list of available charts, please enter 'list'.
            """)
    else:
        chart_type = CHART_TYPE
    return chart_type

def set_email():
    if APP_ENV == "development":
        email = input("Please enter 'y' if you want to send an email. If not, enter 'n.'")
    else:
        email = 'n'
    return email 

def set_recipient_email_address():
    if APP_ENV == "development":
        recipient_address = input("Please enter a recipient's email address")
    else:
        recipient_address = 'ss4012@georgetown.edu'
    return recipient_address

#
# retrieve data from billboard chart
# 

def get_chart(chart_type, birth_date):
    chart = billboard.ChartData(chart_type, birth_date)
    clean_data = []
    for entry in chart.entries:
        x = entry
        data = {
        "title": str(entry)
        }
        clean_data.append(data["title"])
    return clean_data

def get_chart_for_email(chart_type, birth_date):
    chart = billboard.ChartData(chart_type, birth_date)
    chart_for_email = []
    for entry in chart.entries:
        data = {
        "title": entry.title,
        "artist":entry.artist
        }
        chart_for_email.append(data)
    json.dumps(chart_for_email)
    return chart_for_email

#
# send an email using sendgrid application
#

def SendDynamic(SENDER_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS, birth_date, chart_type, chart_for_email): #SENDER_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS, chart_type, birth_date, chart_for_email
    """ Send a dynamic email to a list of email addresses

    :returns API response code
    :raises Exception e: raises an exception """
    # create Mail object and populate
    message = Mail(
        from_email=SENDER_EMAIL_ADDRESS,
        to_emails=RECIPIENT_EMAIL_ADDRESS)
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'subject': 'Billboard Chart on Your Birthday!',
        'birth_date': birth_date,
        'chart_type': chart_type,
        'chart_for_email': chart_for_email
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
    #return str(response.status_code) #HERE

#
# run the app
#

if __name__ == "__main__":

    birth_date = set_birth_date()
    chart_type = set_chart_type()

    clean_data = get_chart(chart_type, birth_date)
    print(clean_data)

    send_email = set_email()

    if send_email == 'y':
        chart_for_email = get_chart_for_email(chart_type, birth_date)
        RECIPIENT_EMAIL_ADDRESS = set_recipient_email_address()
        SendDynamic(SENDER_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS, birth_date, chart_type, chart_for_email)
        print(chart_for_email)