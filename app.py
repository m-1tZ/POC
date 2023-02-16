from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "WW91ciBwYWdlIGJlbG9uZ3MgdG8gbTF0Wg=="
