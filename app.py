from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load structured responses
with open("responses.json", encoding="utf-8") as f:
    responses = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"].lower()
    result = responses.get("default")

    for key, value in responses.items():
        if key != "default" and key in msg:
            result = value
            break

    # Build response HTML
    html = f"<p><strong>Advice:</strong> {result['advice']}</p>"

    if result['symptoms'] or result['treatment'] or result['prevention']:
        html += "<table border='1' cellpadding='5'>"
        html += "<tr><th>Aspect</th><th>Details</th></tr>"
        html += f"<tr><td>Symptoms</td><td>{', '.join(result['symptoms']) or '-'}</td></tr>"
        html += f"<tr><td>Treatment</td><td>{', '.join(result['treatment']) or '-'}</td></tr>"
        html += f"<tr><td>Prevention</td><td>{', '.join(result['prevention']) or '-'}</td></tr>"
        html += "</table>"

    return jsonify({"response": html})

if __name__ == "__main__":
    app.run(debug=True)




'''
#previous without table advise

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load all responses from the JSON file
with open("responses.json", encoding="latin-1") as f:
    responses = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"].lower()
    reply = responses.get("default")
    for key in responses:
        if key != "default" and key in msg:
            reply = responses[key]
            break
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
'''    





