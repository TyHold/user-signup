from flask import Flask, request, render_template, redirect
import re
app= Flask(__name__)
app.config['DEBUG'] = True



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        
        username_err = ''
        password_err = ''
        verify_err = ''
        email_err = ''
        
        EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        if not username or len(username) > 20 or len(username) < 3:
                username_err = "invalid username"
        if not password or len(password) > 20 or len(password) < 3:
                password_err = "invalid password"
        if password != verify:
            verify_err = "passwords do not match"
        if email:
            if not EMAIL_REGEX.match(email) or len(email) > 20 or len(email) < 3 or " " in email:
                email_err = "invalid email"
        if username_err or password_err or verify_err or email_err:
            return render_template("signup.html", username_err=username_err, password_err=password_err, verify_err=verify_err, email_err=email_err)
        else:
            return render_template("signup_confirmation.html", username=username)

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()