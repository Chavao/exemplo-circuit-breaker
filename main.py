from flask import Flask

import service


app = Flask(__name__)


@app.route("/")
def first_method():
    try:
        response = service.first_method()
    except Exception:
        return "Failed\n"

    return response


@app.route("/second")
def second_method():
    try:
        response = service.second_method()
    except Exception:
        return "Failed\n"

    return response
