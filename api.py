from flask import Flask, json, request
from db.dataLayer import DataLayer

app = Flask(__name__)

dataLayer = DataLayer()


@app.route("/student")
def get_student_by_firstName():
    firstName = request.args.get("firstName")
    student = dataLayer.get_student(firstName)
    resp = app.response_class(response=(student.to_json()),
                              status=200,
                              mimetype="application/json")
    return resp


@app.route("/existing_skills")
def get_existing_skills_student():
    existingSkill = request.args.get("skill")
    student = dataLayer.get_existing_skill(existingSkill)
    resp = app.response_class(response=(student.to_json()),
                              status=200,
                              mimetype="application/json")
    return resp


# fetch existing_skills student / skill
# desired student skill / skill


if __name__ == "__main__":
    app.run()
