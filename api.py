from flask import Flask, json, request
from db.dataLayer import DataLayer

app = Flask(__name__)

dataLayer = DataLayer()


@app.route("/user")
def get_user():
    username = request.args.get("firstName")
    user = dataLayer.get_user(username)
    resp = app.response_class(response=(user.to_json()),
                              status=200,
                              mimetype="application/json")

    return resp


if __name__ == "__main__":
    app.run()
