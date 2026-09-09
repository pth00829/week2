import os
from dotenv import load_dotenv
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def move():
    return render_template('index.html')

@app.route('/sign_up',methods=["POST","GET"])
def user():
    if request.method=="POST":
        id=request.form.get('new_id')
        pw=request.form.get('new_pw')
        with open("data.txt", "r") as f:
            saved_data=f.readlines()
            for line in saved_data:
                parts=line.strip().split(":")
                saved_id,saved_pw=parts
                if saved_id==id:
                    return render_template('sign_up.html')
            new_data=f"{id}:{pw}\n"

        with open("data.txt", "a") as f:
            f.write(new_data)
        return render_template("index.html")
    return render_template('sign_up.html')

@app.route('/login',methods=["POST","GET"])
def compare_data():
    if request.method=="POST":
        id=request.form.get('id')
        pw=request.form.get('pw')

        with open("data.txt","r") as f:
            saved_data=f.readlines()
            for line in saved_data:
                parts=line.strip().split(":")
                saved_id,saved_pw=parts
                if saved_id==id and saved_pw==pw:
                    return render_template('success_login.html')

    return render_template('login.html')

@app.route('/secession',methods=["POST","GET"])
def delete_data():
    if request.method=="POST":
        id=request.form.get("delete_id")
        pw=request.form.get("delete_pw")
        new_data=[]

        with open("data.txt", "r") as f:
            data=f.readlines()
            for line in data:
                parts=line.strip().split(":")
                saved_id,saved_pw=parts

                if id==saved_id and pw==saved_pw:
                    continue
                else:
                    new_data.append(line)

        with open("data.txt", "w") as f:
            f.writelines(new_data)
        return render_template('index.html')

    return render_template('secession.html')

if __name__=="__main__":
    app.run(debug=True)