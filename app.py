import os
from dotenv import load_dotenv
from flask import Flask,request,render_template
from mysql import delete_user,save_data,load_data

app=Flask(__name__)

@app.route('/')
def move():
    return render_template('index.html')

@app.route('/sign_up',methods=["POST","GET"])
def user():
    if request.method=="POST":
        id=request.form.get('new_id')
        pw=request.form.get('new_pw')
        save_data(id,pw)
        return render_template("index.html")
    return render_template('sign_up.html')

@app.route('/login',methods=["POST","GET"])
def compare_data():
    if request.method=="POST":
        id=request.form.get('id')
        pw=request.form.get('pw')
        result=load_data(id,pw)
        saved_id,saved_pw=result
        if saved_id==id and saved_pw==pw:
            return render_template('success_login.html')

    return render_template('login.html')

@app.route('/secession',methods=["POST","GET"])
def delete_data():
    if request.method=="POST":
        id=request.form.get("delete_id")
        pw=request.form.get("delete_pw")
        delete_user(id,pw)
        return render_template('index.html')

    return render_template('secession.html')

if __name__=="__main__":
    app.run(debug=True)