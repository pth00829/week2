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

class File:
    def __init__(self):
        self.create_table()

    def create_table(self):
        sql='''
        CREATE TABLE IF NOT EXISTS file(
        user_id varchar(20),
        board_id INT,
        file_name varchar(100) PRIMARY KEY,
        CONSTRAINT fk_data1 FOREIGN KEY (user_id)
            REFERENCES data(user_id)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT fk_board FOREIGN KEY (board_id)
            REFERENCES board(board_id)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
        '''
        with db.cursor() as cursor:
            cursor.execute(sql)
            db.commit()

    def save_file(self,user_id,board_id,file_name):
        sql='''
        INSERT INTO file(user_id,board_id,file_name)
        VALUES(%s,%s,%s);
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[user_id,board_id,file_name])
            db.commit()

    def load_file(self,board_id):
        sql='''
        SELECT file_name
        FROM file
        WHERE board_id=%s;
        '''

        with db.cursor() as cursor:
            cursor.execute(sql,[board_id])
            result=cursor.fetchone()
        return result