import os
from dotenv import load_dotenv
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def move():
    return render_template('index.html')

@app.route('/sign_up',methods=["POST","GET"])
def user():
    return render_template('sign_up.html')

@app.route('/login',methods=["POST","GET"])
def compare_data():
    return render_template('login.html')

@app.route('/secession',methods=["POST","GET"])
def delete_data():
    return render_template('secession.html')

if __name__=="__main__":
    app.run(debug=True)