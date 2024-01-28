from flask import Flask, redirect, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('main.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/CreateAccount")
def signUp():
    return render_template('CreateAccount.html')

@app.route("/FAQ")
def faq():
    return render_template('FAQ.html')

@app.route("/PreTest")
def pretest():
    return render_template('ApplyNow.html')

@app.route("/EmployeeHome")
def employeehome():
    return render_template('employeemain.html')

@app.route("/EmployeeFAQ")
def employeefaq():
    return render_template('employeeFAQ.html')

@app.route("/EmployeeAbout")
def employeeabout():
    return render_template('employeeAbout.html')

@app.route("/EmployeeValues")
def employeevalues():
    return render_template('employeeAbout.html')

@app.route("/rahe")
def secretcord():
    return render_template('secret.html')


if __name__ == "__main__":
    app.run(debug=True)
