# web_app/routes/birthday_routes.py

from flask import Blueprint, request, jsonify

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