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
def save_user():
    if request.method=="POST": # 처음 웹페이지에 접속할 때 GET으로 받기 때문에 POST로 받아야 데이터베이스 속 내용을 수정하거나 새로운 내용을 추가하는 등 post의 행위가 실행된다.
        id=request.form.get('new_id') # request.form.get()은 플라스크 웹서버에서 POST 방식으로 전송된 폼(FORM) 데이터 중 특정 이름의 값을 가져오는 함수
        pw=request.form.get('new_pw')
        login=save_data(id,pw) # mysql.py에서 정의한 함수로 데이터베이스에 회원가입한 id와 pw를 저장한다. 
        if login:
            return redirect(url_for('basic')) # 기존 render_template()를 사용했을때는 새로고침을 하면 브라우저가 이전 요청을 다시 전송을 하고 URL이 변경되지 않았지만 redirect를 사용하면 URL 주소 자체를 교체한다. 
                                          # 교체할 url은 url_for()속 함수를 사용하는 route의 주소이다.
        else:
            return redirect(url_for("save_user1"))
    return render_template('sign_up.html')

@app.route('/sign_up1',methods=["POST","GET"])
def save_user1():
    if request.method=="POST": # 처음 웹페이지에 접속할 때 GET으로 받기 때문에 POST로 받아야 데이터베이스 속 내용을 수정하거나 새로운 내용을 추가하는 등 post의 행위가 실행된다.
        id=request.form.get('new_id1') # request.form.get()은 플라스크 웹서버에서 POST 방식으로 전송된 폼(FORM) 데이터 중 특정 이름의 값을 가져오는 함수
        pw=request.form.get('new_pw1')
        login=save_data(id,pw) # mysql.py에서 정의한 함수로 데이터베이스에 회원가입한 id와 pw를 저장한다. 
        if login:
            return redirect(url_for('basic')) # 기존 render_template()를 사용했을때는 새로고침을 하면 브라우저가 이전 요청을 다시 전송을 하고 URL이 변경되지 않았지만 redirect를 사용하면 URL 주소 자체를 교체한다. 
                                          # 교체할 url은 url_for()속 함수를 사용하는 route의 주소이다.
        else:
            return redirect(url_for("save_user1"))
    return render_template('sign_up1.html')

@app.route('/login',methods=["POST","GET"]) # login도 id와 pw를 입력받기 때문에 methods에 POST와 GET이 필수이다.
def compare_data():
    if request.method=="POST":
        id=request.form.get('id')
        pw=request.form.get('pw')
        result=load_data(id,pw) # mysql.py에 저장된 load_data 함수를 사용했고 역할은 database에 저장된 id, pw를 입력받은 id,pw와 비교하여 일치하면 튜플로 받아온다.
        if result!=None:
            saved_id,saved_pw=result # database에서 받아온 튜플 즉 id, pw를 언패킹한다.
            if saved_id==id and saved_pw==pw: # database 속 id, pw와 입력받은 id, pw가 일치하면
                session['user_id']=saved_id # session['user_id']에 id만 저장한다. id만 저장하는 이유는 id는 중복이 될 수 없기 때문이다. 
                                        # session의 역할은 HTTP는 Stateless 특성으로 인해 이전의 상태를 기억하지 못하기에 session을 이용해 유일한 id를 저장하고 secret_key를 이용해 암호화하여 브라우저 쿠키에 보낸다.
                                        # 쿠키는 페이지를 요청할 때마다 쿠키를 같이 전송하여 누가 보낸 요청인지 서버에 알려준다.
                return redirect(url_for('success_login')) # session으로 인해 위의 조건을 만족하지 못하면 /login/success 로 접속이 불가능하다.
        else:
            return redirect(url_for('compare_data1')) # JS를 이용하여 에러메시지를 띄울 생각

    return render_template('login.html')

@app.route('/login_',methods=["GET","POST"])
def compare_data1():
    if request.method=="POST":
        id=request.form.get('id1')
        pw=request.form.get('pw1')
        result=load_data(id,pw) # mysql.py에 저장된 load_data 함수를 사용했고 역할은 database에 저장된 id, pw를 입력받은 id,pw와 비교하여 일치하면 튜플로 받아온다.
        if result!=None:
            saved_id,saved_pw=result # database에서 받아온 튜플 즉 id, pw를 언패킹한다.
            if saved_id==id and saved_pw==pw: # database 속 id, pw와 입력받은 id, pw가 일치하면
                session['user_id']=saved_id # session['user_id']에 id만 저장한다. id만 저장하는 이유는 id는 중복이 될 수 없기 때문이다. 
                                        # session의 역할은 HTTP는 Stateless 특성으로 인해 이전의 상태를 기억하지 못하기에 session을 이용해 유일한 id를 저장하고 secret_key를 이용해 암호화하여 브라우저 쿠키에 보낸다.
                                        # 쿠키는 페이지를 요청할 때마다 쿠키를 같이 전송하여 누가 보낸 요청인지 서버에 알려준다.
                return redirect(url_for('success_login')) # session으로 인해 위의 조건을 만족하지 못하면 /login/success 로 접속이 불가능하다.
        else:
            return redirect(url_for('compare_data1'))
    return render_template('login1.html')

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
    session.pop('user_id',None) # session 속 user_id를 삭제한다. 그 이유는 삭제하지 않으면 브라우저를 닫아도 session이 남아서 다른 사람이 사용할 수 있다.
                                # 또한 None를 활용한 이유는 이미 삭제되어 있는 상태에서 다시 눌렀을 때 None를 주지않으면 KeyError가 발생하기에 이를 방지하고자 넣었다.
    return redirect(url_for('basic'))

if __name__=="__main__":
    app.run(debug=True)