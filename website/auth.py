from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 3:
            flash('Email must be greater than 2 characters long.', category="error")
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters long.', category="error")
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 characters long.', category="error")
        elif password != password2:
            flash('Passwords must match.', category="error")
        elif len(password) < 3:
            flash('Password must be greater than 2 characters long.', category="error")
        else:
            flash('Successfully signed up!', category="success")

    return render_template('sign_up.html')

