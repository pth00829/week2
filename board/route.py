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
            title=request.form.get('title')
            data_sql=Data_MySql(user_id)
            data_sql.save_data(title,data)
            if data is not None:
                return jsonify({'success':True,'title':title,'content':data})
            else:
                return jsonify({
                    'success':False,
                    'content':'저장된 data가 없습니다.'
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
        result=data_sql.load_data()
        if result is not None:
            return jsonify({"success":True,'title':result[0],'content':result[1]})
        else:
            return jsonify({"success":False,'title':None,'content':None})

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

@board_bp.route('/main/search',methods=["GET","POST"])
def show_search_data():
    user_id=session.get('user_id')
    if user_id:
        if request.method=="POST":
            data=request.form.get('search_txt')
            if data!="":
                search_range=request.form.get('choose')
                data_mysql=Data_MySql(user_id)
                result=data_mysql.search_data(search_range,data)
                if result:
                    return jsonify({"success":True,"data":result})
                else:
                    return jsonify({"success":False,"message":"검색 결과가 없습니다."})
            else:
                return jsonify({"success":False,"message":"검색어를 입력해주세요"})
        else:
            return render_template('search.html')
    else:
        return redirect(url_for('basic'))