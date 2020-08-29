from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import datetime, os

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', nachricht='Hello World!')\

@app.route('/status')
def status():
    time = datetime.datetime.utcnow()
    user = os.getlogin()
    return render_template('status.html', time=time, user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
