import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime
from app import APP_ENV
import billboard #added
import json #added

# .env file should have SENDGRID_API_KEY and SENDER_EMAIL_ADDRESS variables
load_dotenv()

#
# user input
#

BIRTH_DATE = os.getenv("BIRTH_DATE", default="2000-01-01")
CHART_TYPE = os.getenv("CHART_TYPE", default="hot-100")

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



# value errors are handled by billboard.py --> no need to add more input validation

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


if __name__ == "__main__":

    birth_date = set_birth_date()
    chart_type = set_chart_type()

    print_chart = get_chart(chart_type, birth_date) #test
    print(print_chart) #test

