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
    return render_template('About.html')

@app.route("/CreateAccount")
def signUp():
    return redirect('/NavBarLinks/CreateAccount.html')

@app.route("/FAQ")
def faq():
    return redirect('/NavBarLinks/FAQ.html')
 
if __name__ == "__main__":
    app.run(debug=True)
