from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates', )


@app.route('/')
def homepage():
    return render_template('html/HomePage.html')


@app.route('/login')
def login():
    return render_template('html/LoginPage.html')


@app.route('/register')
def register():
    return render_template('html/RegisterAccountPage.html')


@app.route('/newpassword')
def forgotpassword():
    return render_template('html/ForgotPasswordPage.html')


@app.route('/confirmation')
def confirm():
    return render_template('html/ConfirmationPage.html')


if __name__ == '__main__':
    app.run(debug=True)
