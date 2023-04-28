from flask import Flask

app = Flask(__name__)

@app.route("/result", methods = ["POST", "GET"])

def result():
    return {"API":"Response Positive"}

if _name_=='_main_':
    app.run(debug = True , port = 2000) 