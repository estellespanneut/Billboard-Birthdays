# web_app/routes/birthday_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.birthday import get_chart
from app.birthday import SendDynamic
from app.birthday import get_chart_for_email

birthday_routes = Blueprint("birthday_routes", __name__)

@birthday_routes.route("/birthday/billboard.json")
def birthday_billboard_api():
    print("Birthday Billboard (API)...")
    print("URL PARAMS:", dict(request.args))

    BIRTH_DATE = request.args.get("birth_date") or "2000-01-01" 
    CHART_TYPE = request.args.get("chart_type") or "hot-100"

    results = get_chart(chart_type=CHART_TYPE, birth_date=BIRTH_DATE)
    print(results)
    print(type(results))
    print(dir(results))
    #breakpoint()

    if results: 
        return jsonify(results) 
        #return "about me"
    else:
        return jsonify({"message":"Invalid Information. Please try again."}), 404


@birthday_routes.route("/birthday/form")
def birthday_form():
    print("BIRTHDAY FORM...")
    return render_template("birthday_form.html")

@birthday_routes.route("/birthday/billboard", methods=["GET", "POST"])
def birthday_billboard(): #check this
    print("BIRTHDAY BOARD...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    BIRTH_DATE = request_data.get("birth_date") or "2000-01-01" 
    CHART_TYPE = request_data.get("chart_type") or "hot-100"
    
    results = get_chart(chart_type=CHART_TYPE, birth_date=BIRTH_DATE)
    if results:
        flash("Birthday Data Generated Successfully!", "success")
        return render_template("birthday_billboard.html", chart_type=CHART_TYPE, birth_date=BIRTH_DATE, results=results)
    else:
        flash("Error. Please try again!", "danger")
        return redirect("/birthday/form")

@birthday_routes.route("/birthday/email", methods=["GET", "POST"])
def birthday_email(): #check this
    print("Email sending!")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    BIRTH_DATE = request_data.get("birth_date") or "2000-01-01" 
    CHART_TYPE = request_data.get("chart_type") or "hot-100"
    CHART_FOR_EMAIL = get_chart_for_email(birth_date = BIRTH_DATE, chart_type = CHART_TYPE)
    SENDER_EMAIL_ADDRESS = request_data.get("SENDER_EMAIL_ADDRESS") or "example@example.com"
    results = SendDynamic(SENDER_EMAIL_ADDRESS = SENDER_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS = SENDER_EMAIL_ADDRESS, birth_date = BIRTH_DATE, chart_type = CHART_TYPE, chart_for_email = CHART_FOR_EMAIL)
    #results = SendDynamic(SENDER_EMAIL_ADDRESS = SENDER_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS = SENDER_EMAIL_ADDRESS) #recipient_address = SENDER_EMAIL_ADDRESS
    
    if results:
        flash("Email sent successfully!", "success")
        return render_template("email.html", recipient_address = SENDER_EMAIL_ADDRESS)
    else:
        flash("Error. Please try again!", "danger")
        return redirect("/birthday/billboard")