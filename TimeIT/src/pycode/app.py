from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def homepage():
    return render_template('html/homepage.html')


@app.route('/login')
def login():
    return render_template('html/login.html')


if __name__ == '__main__':
    app.run(debug=True)
