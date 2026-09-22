import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db=pymysql.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME'),
    charset='utf8'
)

class MySql:
    def __init__(self): # 객체 생성 후 인자 없이 메서드 호출을 가능하게 하기 위해 id,pw,data등을 인스턴스 변수로 선언헀다.
        self.create_table()

    def create_table(self):
        sql='''
        CREATE TABLE IF NOT EXISTS data(
        user_id varchar(20) PRIMARY KEY,
        user_pw varchar(20),
        user_name varchar(20),
        user_school varchar(20)
        )
        '''
        with db.cursor() as cursor:
            cursor.execute(sql)
            db.commit()

    def save_data(self,id,pw,name,school):
        sql='''
        SELECT user_id
        FROM data
        WHERE user_id=%s;
        '''
        with db.cursor() as cursor:
            cursor.execute(sql,[id])
            result=cursor.fetchone()
            db.commit()

        if result is None:
            sql='''
            INSERT INTO data(user_id,user_pw,user_name,user_school)
            VALUES(%s,%s,%s,%s);
            '''

            with db.cursor() as cursor:
                cursor.execute(sql,[id,pw,name,school])
                db.commit()

            return True
        else:
            return False

    def load_data(self,id,pw):
        sql='''
        SELECT user_id,user_pw
        FROM data
        WHERE user_id=%s and user_pw=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[id,pw])
            result=cursor.fetchone()
            db.commit()

        if result is None:
            return None
        else:
            return result

    def delete_data(self,id,pw):

        result=self.load_data()
        if result is not None:
            sql='''
            DELETE FROM data
            WHERE user_id=%s and user_pw=%s;
            '''
            with db.cursor() as cursor:
                cursor.execute(sql,[id,pw])
                db.commit()
            return True
        else:
            return False

    def find_data(self,name,school):
        sql='''
        SELECT user_id,user_pw
        FROM data
        WHERE user_name=%s and user_school=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[name,school])
            result=cursor.fetchall()
        return result

    def change_pw(self,id,pw,name,school):
        sql='''
        UPDATE data
        SET user_pw=%s
        WHERE user_id=%s and user_name=%s and user_school=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[pw,id,name,school])
            db.commit()

    def load_all(self,id):
        sql='''
        SELECT user_name,user_school
        FROM data
        WHERE user_id=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[id])
            result=cursor.fetchone()
        return result

    def edit_data(self,id,name,school):
        sql='''
        UPDATE data
        SET user_name=%s, user_school=%s
        WHERE user_id=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[name,school,id])
            