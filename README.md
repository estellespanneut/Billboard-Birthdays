# Billboard-Birthdays

This app shows you a chosen billboard chart data of a selected date. It also sends a customized birthday card to a specified email address.

![](https://i.ibb.co/1T9r5hL/example-email.png)


## Installation

Fork [this repo](https://github.com/estellespanneut/Billboard-Birthdays), then clone or download the forked repo onto your local computer (for example to the Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/Billboard-Birthdays/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "billboard-env":

```sh
conda create -n billboard-env python=3.8
conda activate billboard-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API key (i.e. `SENDGRID_API_KEY`).

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"

```

## Usage

Retrieve data from the selected chart of the selected date & email the results

```sh
python -m app.birthday

# in production mode:
APP_ENV="production" BIRTH_DATE="2000-01-01" CHART_TYPE="hot-100" python -m app.birthday
```

> NOTE: the SendGrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")


### Web App

```sh
# mac:
FLASK_APP=web_app flask run
# windows:
export FLASK_APP=web_app
flask run
```

### Heroku app

go to http://birthday-app-2021.herokuapp.com/ and follow instructions located in the web app


