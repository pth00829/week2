from flask import Blueprint,request,redirect,session,url_for,render_template,jsonify,send_file
import os
from dotenv import load_dotenv
from data_sql import Data_MySql
from mysql import MySql
from file import File

board_bp=Blueprint('board',__name__,url_prefix='/board')

@board_bp.route('/main')
def board():
    user_id=session.get('user_id')
    if user_id:
        return render_template('all_board.html')
    else:
        return redirect(url_for('basic'))

@board_bp.route('/main/create',methods=["POST","GET"])
def success_login():
    user_id=session.get('user_id')
    if not user_id:
        return redirect(url_for('user.compare_data'))
    else:
        if request.method=="POST":
            data_sql=Data_MySql(user_id)
            data=request.form.get('textarea')
            title=request.form.get('title')
            files=request.files.get('file')
            if request.form.get('secret')=='true':
                secret=True
                secret_pw=request.form.get('secret_pw')
            else:
                secret=False
                secret_pw=None
            board_id=data_sql.save_data(title,data,secret,secret_pw)
            file=File()
            if files:
                files.save('./uploads/'+files.filename)
                file_name=files.filename
                file.save_file(user_id,board_id,file_name)
            
            if data is not None:
                data_sql.load_all()
                return jsonify({'success':True,'title':title,'content':data})
            else:
                return jsonify({
                    'success':False,
                    'content':'저장된 data가 없습니다.'
                })
        else:
            return render_template('new_board.html')

@board_bp.route('/main/data')
def db_data():
    user_id=session.get('user_id')
    data_sql=Data_MySql(user_id)
    if not user_id:
        return redirect(url_for('user.compare_data'))
    else:
        result=data_sql.load_data()
        if result is not None:
            return jsonify({"success":True,'board_id':result[0],'title':result[1],'content':result[2]})
        else:
            return jsonify({"success":False,'title':None,'content':None})

@board_bp.route('/main/delete')
def delete_db():
    user_id=session.get('user_id')
    if user_id:
        data_mysql=Data_MySql(user_id)
        board_id=request.args.get('board_id')

        if data_mysql.delete_db_data(board_id):
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

@board_bp.route('/check',methods=['POST'])
def check():
    user_id=session.get('user_id')
    if user_id:
        if request.method=='POST':
            board_id=request.form.get('board_id')
            data_mysql=Data_MySql(user_id)
            result=data_mysql.check_user(board_id)
            if result:
                return jsonify({'success':True})
            else:
                return jsonify({'success':False})

@board_bp.route('/main/correction',methods=["POST","GET"])
def correction():
    user_id=session.get('user_id')
    if user_id:
        if request.method=='POST':

            return jsonify({"success":True})
        else:
            board_id=request.args.get('board_id')
            data_mysql=Data_MySql(user_id)
            result=data_mysql.load_data(board_id)
            return render_template('update_board.html')
    else:
        return redirect(url_for('basic'))

@board_bp.route('/main/correction/data',methods=["GET"])
def correction_data():
    user_id=session.get('user_id')
    if user_id:
        board_id=request.args.get('board_id')
        file=File()
        file_name=file.load_file(board_id)
        if file_name:
            filename=file_name[0]
        else:
            filename=None
        data_mysql=Data_MySql(user_id)
        result=data_mysql.load_data(board_id)
        title,content,secret,secret_pw,id=result
        return jsonify({
            'success':True,
            'title':title,
            'content':content,
            'secret':secret,
            'secret_pw':secret_pw,
            'file_name':filename,
            'user_id':id})
    else:
        return redirect(url_for('basic'))

@board_bp.route('/main/correction/update',methods=["POST","GET"])
def update_data():
    user_id=session.get('user_id')
    if user_id:
        data_mysql=Data_MySql(user_id)
        title=request.form.get('title')
        content=request.form.get('textarea')
        board_id=request.args.get('board_id')
        file1=File()
        file=request.files.get('file')
        if file:
            file.save('./uploads/'+file.filename)
            file_name=file.filename
            file1.save_file(user_id,board_id,file_name)

        if request.form.get('secret')=='true':
            secret=True
            secret_pw=request.form.get('secret_pw')
        else:
            secret=False
            secret_pw=None
        data_mysql.update_data(title,content,board_id,secret,secret_pw)
        return jsonify({'success':True,'message':'수정을 완료하였습니다.'})
    else:
        return redirect(url_for('basic'))

@board_bp.route('/')
def main():
    user_id=session.get('user_id')
    if user_id:
        data_mysql=Data_MySql(user_id)
        result=data_mysql.load_all()
        if result:
            return jsonify({'success':True,'data':result})
        else:
            return jsonify({"success":False,'message':'저장된 게시글이 없습니다.'})
    else:
        return redirect(url_for('basic'))

@board_bp.route('/look')
def look_board():
    user_id=session.get('user_id')
    if user_id:
        return render_template('one_board.html')
    else:
        return redirect(url_for('basic'))

@board_bp.route('/profile')
def user_profile():
    user_id=session.get('user_id')
    if user_id:
        return render_template('profile.html')
    else:
        return redirect(url_for('basic'))

@board_bp.route('/profile/get-data')
def profile_data():
    user_id=request.args.get('user_id',session.get('user_id'))
    if user_id:
        mysql=MySql()
        result=mysql.load_all(user_id)
        name,school,image=result
        if image:
            image_exist=True
        else:
            image_exist=False
        if user_id==session.get('user_id'):
            return jsonify({'success':True,
                            'btn':True,
                            'name':name,
                            'school':school,
                            'image':image,
                            'image_exist':image_exist})
        else:
            return jsonify({'success':False,
                            'btn':False,
                            'name':name,
                            'school':school,
                            'image':image,
                            'image_exist':image_exist})
    else:
        return redirect(url_for('basic'))

@board_bp.route('/profile/edit')
def edit_profile():
    return render_template('edit_profile.html')

@board_bp.route('/profile/edit-data',methods=['POST'])
def edit_user_data():
    user_id=session.get('user_id')
    if user_id:
        name=request.form.get('user_name')
        school=request.form.get('user_school')
        file=request.files.get('fileImage')
        if file:
            file.save('./static/uploads/'+file.filename)
            image_name=file.filename
        else:
            image_name=None
        mysql=MySql()
        mysql.edit_data(user_id,name,school,image_name)
        if image_name:
            return jsonify({'success':True})
        else:
            return jsonify({'success':False})
    else:
        return redirect(url_for('basic'))

@board_bp.route('/download',methods=['POST'])
def download():
    if request.method=="POST":
        path='./uploads/'
        return send_file(path+request.form.get('file_name'),as_attachment=True)
    else:
        redirect(url_for('board.board'))

@board_bp.route('/profile/other')
def other_profile():
    return render_template('other_profile.html')

