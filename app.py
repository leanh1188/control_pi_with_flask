from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import datetime, os

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    now = datetime.datetime.utcnow()
    time = now.strftime('%d-%m-%Y %H:%M')
    return render_template('index.html', time=time)\

@app.route('/status')
def status():
    user = os.getlogin()
    return render_template('status.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
