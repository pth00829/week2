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
        user_id varchar(20),
        board_id INT AUTO_INCREMENT PRIMARY KEY,
        title varchar(100),
        content TEXT,
        CONSTRAINT fk_data FOREIGN KEY (user_id)
            REFERENCES data(user_id)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        '''

        with db.cursor() as cursor:
            cursor.execute(sql)
            db.commit()

    def save_data(self,title,content):

        sql1='''
        INSERT INTO board(user_id,title,content)
        VALUES(%s,%s,%s)
        '''

        with db.cursor() as cursor:
            cursor.execute(sql1,[self.id,title,content])
            db.commit()

    def load_data(self,board_id):
        sql='''
        SELECT title, content
        FROM board
        WHERE user_id=%s and board_id=%s
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[self.id,board_id])
            result=cursor.fetchone()

        return result

    def delete_db_data(self,board_id):
        sql='''
        DELETE FROM board
        WHERE user_id=%s and board_id=%s;
        '''

        sql1='''
        SELECT user_id
        FROM board
        WHERE user_id=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql1,[self.id])
            result=cursor.fetchone()
            if result is not None:
                cursor.execute(sql,[self.id,board_id])
                db.commit()
                return True
            else:
                return False

    def search_data(self,search_range,data):
        if search_range=='title':
            value='%'+data+'%'
            sql='''
            SELECT board_id, title,content
            FROM board
            WHERE title LIKE %s; 
            '''

            with db.cursor() as cursor:
                cursor.execute(sql,[value])
                result=cursor.fetchall()
                db.commit()
            return result
        elif search_range=='content':
            value='%'+data+'%'
            sql='''
            SELECT board_id, title,content
            FROM board
            WHERE content LIKE %s; 
            '''

            with db.cursor() as cursor:
                cursor.execute(sql,[value])
                result=cursor.fetchall()
                db.commit()
            return result
        
        elif search_range=='all':
            value='%'+data+'%'
            sql='''
            SELECT board_id, title,content
            FROM board
            WHERE title LIKE %s or content LIKE %s; 
            '''

            with db.cursor() as cursor:
                cursor.execute(sql,[value,value])
                result=cursor.fetchall()
                db.commit()
            return result

    def update_data(self,title,content,board_id):
        sql2='''
        UPDATE board
        SET title=%s, content=%s
        WHERE user_id=%s and board_id=%s
        '''

        with db.cursor() as cursor:
            cursor.execute(sql2,[title,content,self.id,board_id])
            db.commit()

    def load_all(self):
        sql='''
        SELECT board_id,title,content
        FROM board
        WHERE user_id=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[self.id])
            result=cursor.fetchall()

        return result