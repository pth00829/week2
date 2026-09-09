import pymysql
import os
from dotenv import load_dotenv

load_dotenv() # 비밀번호나 중요 정보를 가리기 위해 하드코딩하지 않고 .env를 사용
db=pymysql.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME'),
    charset='utf8'
)


def save_data(id,pw): # 데이터를 저장하는 함수
    
    sql1='''
    SELECT user_id
    FROM data
    WHERE user_id=%s
    ''' # 데이터베이스 속에 입력한 id와 일치하는 user_id가 있는지 확인 
    with db.cursor() as cursor: # cursor()을 이용해 데이터베이스에 전달
        cursor.execute(sql1,[id]) # 전달한 내용들을 실행시킨다.
        result=cursor.fetchone() # 전달한 내용들 중 하나를 받아온다. 입력한 id와 일치하는 id가 존재하더라도 PRIMARY KEY로 지정을 해두었기 때문에 database에는 하나만 존재한다. 

    if result==None: # id가 일치하지않으면
        data=[id,pw] # excute가 리스트나 튜플만 받음
        sql2='''
        INSERT INTO data(user_id,user_pw)
        VALUES(%s,%s)
        ''' # database에 없던 아이디이기 때문에 회원가입 성공 즉, 아이디와 비번을 추가하라는 명령
        with db.cursor() as cursor: # 데이터베이스에 전달을 위해 생성
            cursor.execute(sql2,data) # 내용들을 실행시킨다
            db.commit() 
    else:
        print("아이디 있음") # 아직 구현 실패 아이디가 있을경우 JS를 이용하여 팝업창 띄울 생각

def load_data(id,pw): # id, pw 비교를 위해 데이터 로드를 할 함수
    data=[id,pw]
    sql='''
    SELECT user_id,user_pw
    FROM data
    WHERE user_id=%s and user_pw=%s
    '''

    with db.cursor() as cursor:
        cursor.execute(sql,data)
        result=cursor.fetchone()
        db.commit()
    return result # 반환값으로 튜플을 반환한다. 튜플 속에는 (user_id,user_pw)가 있다.
    

def delete_user(id,pw):
    data=[id,pw]
    sql='''
    DELETE FROM data
    WHERE user_id=%s and user_pw=%s
    ''' # id와 pw를 삭제하라는 명령

    with db.cursor() as cursor:
        cursor.execute(sql,data)
        db.commit()