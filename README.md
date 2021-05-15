# Billboard-Birthdays

Sends you a customized email every morning, with information of interest, such as the upcoming weather forecast for your zip code.

![](https://user-images.githubusercontent.com/1328807/77860069-173ef580-71db-11ea-83c6-5897bb9f4f51.png)



## Configuration

Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API key (i.e. `SENDGRID_API_KEY`).

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"

# optional vars:
#APP_ENV="development"
#COUNTRY_CODE="US"
#ZIP_CODE="10017"
#USER_NAME="Jon Snow"
```

## Usage


Running the app locally:

```sh
python -m app.birthday

# in production mode:
APP_ENV="production" BIRTH_DATE="2000-01-01" CHART_TYPE="hot-100" python -m app.birthday
```


