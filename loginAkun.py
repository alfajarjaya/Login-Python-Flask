from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/templates', methods=['POST'])
def login():
    user = request.form.get('user')
    passwd = request.form.get('password')

    if user == 'admin' and passwd == 'admin':
        return render_template('dbLogin.html', user=user, password=passwd)
    else:
        return render_template('login.html', error='Username / Password salah')

if __name__ == '__main__':
    app.run(debug=True)
