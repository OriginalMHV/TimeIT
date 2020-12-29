from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__, template_folder='templates', )


@app.route('/')
def homepage():
    return render_template('templates/templates/HomePage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('templates/templates/LoginPage.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('RegisterAccountPage.html.html', title='Register', form=form)



@app.route('/getNewPassword')
def getNewPassword():
    return render_template('templates/templates/ForgotPasswordPage.html')


@app.route('/confirmation')
def confirm():
    return render_template('templates/templates/ConfirmationPage.html')


if __name__ == '__main__':
    app.run(debug=True)
