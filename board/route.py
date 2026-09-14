from flask import Blueprint,request,redirect,session,url_for,render_template,jsonify
import os
from dotenv import load_dotenv
from data_sql import Data_MySql

board_bp=Blueprint('board',__name__,url_prefix='/board')

@board_bp.route('/main',methods=["POST","GET"])
def success_login():
    user_id=session.get('user_id')
    if not user_id:
        return redirect(url_for('compare_data'))
    else:
        if request.method=="POST":
            data=request.form.get('textarea')
            data_sql=Data_MySql(user_id)
            data_sql.save_data(data)
            if data is not None:
                return jsonify({'success':True,'data':data})
            else:
                return jsonify({
                    'success':False,
                    'data':'저장된 data가 없습니다.'
                })
        else:
            return render_template('success_login.html')

@board_bp.route('/main/data')
def db_data():
    user_id=session.get('user_id')
    data_sql=Data_MySql(user_id)
    if not user_id:
        return redirect(url_for('user.compare_data'))
    else:
        data=data_sql.load_data()
        if data is not None:
            return jsonify({"success":True,'data':data})
        else:
            return jsonify({"success":False,'data':None})

@board_bp.route('/main/delete')
def delete_db_data():
    user_id=session.get('user_id')
    if user_id:
        data_mysql=Data_MySql(user_id)

        if data_mysql.delete_db_data():
            return jsonify({"success":True})
        else:
            return jsonify({"success":False})
    else:
        return redirect(url_for('basic'))