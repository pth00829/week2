import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

db=pymysql.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME'),
    charset='utf8'
)
# TODO
# 게시판에서 작성한 내용을 user_id가 일치한다면 내용을 저장한다.(user_id는 외래키로 참조하여 로그인된 id를 비교한다.)
class Data_MySql:
    def __init__(self,id):
        self.id=id
        self.create_table()

    def create_table(self):
        sql='''
        CREATE TABLE IF NOT EXISTS board(
        user_id varchar(20) primary key,
        data varchar(1000),
        CONSTRAINT fk_data FOREIGN KEY (user_id)
            REFERENCES data(user_id)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        '''

        with db.cursor() as cursor:
            cursor.execute(sql)
            db.commit()

    def save_data(self,data):
        result=self.load_data()

        if result is None:
            sql1='''
            INSERT INTO board(user_id,data)
            VALUES(%s,%s)
            '''

            with db.cursor() as cursor:
                cursor.execute(sql1,[self.id,data])
                db.commit()
        else:
            sql2='''
            UPDATE board
            SET data=%s
            WHERE user_id=%s
            '''

            with db.cursor() as cursor:
                cursor.execute(sql2,[data,self.id])
                db.commit()

    def load_data(self):
        sql='''
        SELECT data
        FROM board
        WHERE user_id=%s
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[self.id])
            result=cursor.fetchone()

        return result

    def delete_db_data(self):
        sql='''
        DELETE FROM board
        WHERE user_id=%s
        '''

        sql1='''
        SELECT user_id
        FROM board
        WHERE user_id=%s
        '''

        with db.cursor() as cursor:
            cursor.execute(sql1,[self.id])
            result=cursor.fetchone()
            if result is not None:
                cursor.execute(sql,[self.id])
                db.commit()
                return True
            else:
                return False