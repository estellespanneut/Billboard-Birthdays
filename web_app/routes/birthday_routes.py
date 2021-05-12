# web_app/routes/birthday_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.birthday import get_chart

birthday_routes = Blueprint("birthday_routes", __name__)

@birthday_routes.route("/birthday/billboard.json")
def birthday_billboard_api():
    print("Birthday Billboard (API)...")
    print("URL PARAMS:", dict(request.args))

    birth_date = request.args.get("birth_date") or "2000-01-01" 
    chart_type = request.args.get("chart_type") or "hot-100"

    results = get_chart(chart_type=chart_type, birth_date=birth_date)
    print(results)
    print(type(results))
    print(dir(results))
    #breakpoint()

    if results: 
        return jsonify(results) #This gives me an error every time
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

    birth_date = request_data.get("birth_date") or "2000-01-01" #error
    chart_type = request_data.get("chart_type") or "hot-100"
    
    results = get_chart(chart_type=chart_type, birth_date=birth_date)
    if results:
        flash("Birthday Data Generated Successfully!", "success")
        return render_template("birthday_billboard.html", chart_type=chart_type, birth_date=birth_date, results=results)
    else:
        flash("Error. Please try again!", "danger")
        return redirect("/birthday/form")

