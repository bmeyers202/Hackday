from flask import Flask
from flask import g, session, request, url_for, flash
from flask import redirect, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
   app.run(debug=True, port=5001,use_reloader=True)