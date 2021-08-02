import os
from flask import Flask, Blueprint, request, jsonify, render_template
from auth.authmain import auth
app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return "this is home"


@app.route('/app')
def apppage():
    return render_template('app.html')





if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(threaded=True, port=port, debug=True, host='0.0.0.0')
