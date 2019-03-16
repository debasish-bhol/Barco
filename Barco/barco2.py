import app
import json
import flask
from flask import Flask, request
from flask_cors import CORS, cross_origin


app1 = Flask(__name__)
CORS(app1)

@app1.route("/api/", methods=["GET"])
def hello():
    name = request.args.get("city")
    k = app.moveon()
    return json.dumps(k['bhai'][name])

# @app1.route("/api/f/", methods=["GET"])
# def remove_factors():
#     gwt = request.args.get('factor')
#     name = request.args.get('city')

#     if(gwt == "growth"):
#         k = app.moveon12()
#         return json.dumps(k['bhai'][name])
#     elif gwt == "literacy":
#         k = app.moveon13()
#         return json.dumps(k['bhai'][name])
#     elif gwt == "rank":
#         k = app.moveon14()
#         return json.dumps(k['bhai'][name])
    

if __name__ == "__main__":
    app1.run(host = '0.0.0.0',debug=True)

