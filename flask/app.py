from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['fname']
    lname = request.form['lname']
    gender = request.form['gender']
    address = request.form['address']
    countries = request.form['countries']
    sub = request.form['sub[]']
    pwd = request.form ['pwd']
    print(f'Hello {name}, your lname is {lname} , gender is {gender}, address is {address}, countries is {countries}, pwd is {pwd}, sub is {sub}')
    return render_template('registered.html')

if __name__ == '__main__':
    app.run(debug=True)