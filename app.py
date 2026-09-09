import os
from dotenv import load_dotenv
from flask import Flask,request,render_template,redirect,url_for,session
from mysql import delete_user,save_data,load_data

load_dotenv()

app=Flask(__name__)

app.secret_key=os.getenv('SECRET_KEY')

@app.route('/')
def basic():
    return render_template('index.html')

@app.route('/sign_up',methods=["POST","GET"]) # sing_up의 경우 id와 pw를 입력받기 때문에 methods에 POST와 GET이 필수이다.
def user():
    if request.method=="POST": # 처음 웹페이지에 접속할 때 GET으로 받기 때문에 POST로 받아야 데이터베이스 속 내용을 수정하거나 새로운 내용을 추가하는 등 post의 행위가 실행된다.
        id=request.form.get('new_id') # request.form.get()은 플라스크 웹서버에서 POST 방식으로 전송된 폼(FORM) 데이터 중 특정 이름의 값을 가져오는 함수
        pw=request.form.get('new_pw')
        save_data(id,pw)
        return redirect(url_for('basic'))
    return render_template('sign_up.html')

@app.route('/login',methods=["POST","GET"]) # login도 id와 pw를 입력받기 때문에 methods에 POST와 GET이 필수이다.
def compare_data():
    if request.method=="POST":
        id=request.form.get('id')
        pw=request.form.get('pw')
        result=load_data(id,pw)
        saved_id,saved_pw=result
        if saved_id==id and saved_pw==pw:
            session['user_id']=saved_id
            return redirect(url_for('success_login'))
        else:
            return render_template('login.html')

    return render_template('login.html')

@app.route('/secession',methods=["POST","GET"]) # secession 역시 id와 pw를 입력받기 때문에 methods에 POST와 GET이 필수이다.
def delete_data():
    if request.method=="POST":
        id=request.form.get("delete_id")
        pw=request.form.get("delete_pw")
        delete_user(id,pw)
        return redirect(url_for('basic'))

    return render_template('secession.html')

@app.route('/login/success')
def success_login():
    user_id=session.get('user_id')
    if not user_id:
        return redirect(url_for('compare_data'))
    else:
        return render_template('success_login.html')

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('basic'))

if __name__=="__main__":
    app.run(debug=True)