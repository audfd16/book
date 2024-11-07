from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///users.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)



@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/registration", methods = ['POST', 'GET'])
def registration():
    
    if request.method == 'POST':
        Username = request.form['Username']
        Email = request.form['Email']
        password = request.form['password']
        user = Users(username=Username, password=password, email=Email)
        print (Username, Email, password)

        print(engine.url)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
        
    else:
        return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)