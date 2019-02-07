from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home/')
def home():
    return render_template("home.html")


@app.route('/contact_us/')
def contact_us():
    return render_template("contact_us.html")


if __name__ == '__main__':
    app.run()
