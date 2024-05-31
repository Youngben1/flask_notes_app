from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('The Email correct for your eye so??', category='error')
        elif len(firstName) < 3:
            flash('First Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Why your passwords no de match olodo!!', category='error')
        elif len(password1) < 7:
            flash('Na your papa you de give short password', category='error')
        else:
            flash('Account created successfully!!!', category='success')
    
    return render_template("sign_up.html")