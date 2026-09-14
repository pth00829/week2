import os
from dotenv import load_dotenv
from flask import Flask,request,render_template,redirect,url_for,session,jsonify
from data_sql import Data_MySql
from user.main import user_bp
from board.route import board_bp

load_dotenv()

app=Flask(__name__)

app.secret_key=os.getenv('SECRET_KEY')

@user_bp.route('/')
def basic():
    if not session.get('user_id'):
        return render_template('index.html')
    else:
        return redirect(url_for('user.success_login'))

app.register_blueprint(user_bp)
app.register_blueprint(board_bp)

if __name__=="__main__":
    app.run(debug=True)