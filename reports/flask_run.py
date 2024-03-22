from flask import Flask, send_file
from waitress import serve

app = Flask(__name__)


@app.route('/')
def serve_index():
    return send_file('index.html')


@app.route('/TESTS-login.xml')
def serve_login_report():
    return send_file('TESTS-login.xml', mimetype='application/xml')


@app.route('/TESTS-signup.xml')
def serve_signup_report():
    return send_file('TESTS-signup.xml', mimetype='application/xml')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
