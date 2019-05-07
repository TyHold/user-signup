from flask import Flask, request, render_template
app= Flask(__name__)
app.config['DEBUG'] = True

@app.route('/confirm', methods=["POST"])
def confirm():
    username = request.form['Username']
    return render_template("signup_confirmation.html", username=username)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()