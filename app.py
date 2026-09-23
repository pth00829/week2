import os
from dotenv import load_dotenv
from flask import Flask,request,render_template,redirect,url_for,session,jsonify
from data_sql import Data_MySql
from user.main import user_bp
from board.route import board_bp

load_dotenv()

app=Flask(__name__)

UPLOAD_FOLDER='./uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
app.register_blueprint(user_bp)
app.register_blueprint(board_bp)

app.secret_key=os.getenv('SECRET_KEY')

@app.route('/')
def basic():
    if not session.get('user_id'):
        return render_template('index.html')
    else:
        return redirect(url_for('board.board'))

if __name__=="__main__":
    app.run(debug=True)