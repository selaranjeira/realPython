import os
from flask import Flask, render_template


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "ola !"


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')




if __name__ == '__main__':
    app.run(debug=True)
