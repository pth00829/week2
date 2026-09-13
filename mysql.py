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
    def __init__(self,id,pw): # 객체 생성 후 인자 없이 메서드 호출을 가능하게 하기 위해 id,pw,data등을 인스턴스 변수로 선언헀다.
        self.id=id
        self.pw=pw
        self.data=[self.id,self.pw]

    def save_data(self):
        sql='''
        SELECT user_id
        FROM data
        WHERE user_id=%s;
        '''
        with db.cursor() as cursor:
            cursor.execute(sql,[self.id])
            result=cursor.fetchone()
            db.commit()

        if result is None:
            sql='''
            INSERT INTO data(user_id,user_pw)
            VALUES(%s,%s);
            '''

            with db.cursor() as cursor:
                cursor.execute(sql,self.data)
                db.commit()

            return True
        else:
            return False

    def load_data(self):
        sql='''
        SELECT user_id,user_pw
        FROM data
        WHERE user_id=%s and user_pw=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,self.data)
            result=cursor.fetchone()
            db.commit()

        if result is None:
            return None
        else:
            return result

    def delete_data(self):

        result=self.load_data()
        if result is not None:
            sql='''
            DELETE FROM data
            WHERE user_id=%s and user_pw=%s;
            '''
            with db.cursor() as cursor:
                cursor.execute(sql,self.data)
                db.commit()
            return True
        else:
            return False