from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3 
import sys

app = Flask(__name__)
app.secret_key = 'abcd'

@app.route('/')
def first_page():    
    return render_template('first.html')

@app.route('/login',methods=['GET','POST'])
def user_login():
    return render_template('login.html')

@app.route('/exhib', methods=['GET','POST'])
def showexhib():
    db = sqlite3.connect("DB_project_data.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select * from EXHIBITION'
    ).fetchall()
    db.close()
    return render_template('context.html',items=items)

@app.route('/exhib/edit', methods=['GET','POST'])
def editMenu():
    if request.method=='POST':
        db = sqlite3.connect("DB_project_data.db")
        db.row_factory = sqlite3.Row
        query = "SELECT ID,pw FROM USERS WHERE ID = ? and pw=?"
        value=(request.form['uid'],request.form['pw'])
        data=db.execute(query,value).fetchall()
        db.close()
        if data:
            return redirect(url_for('showexhib'))
        else:
            flash('회원 정보가 없습니다.')
            return redirect(url_for('user_login'))

@app.route('/assign', methods=['GET','POST'])
def user_assign():
    return render_template('signup.html')

@app.route('/save', methods=['GET','POST'])
def save_users():
    if  request.method=='POST':
        db = sqlite3.connect("DB_project_data.db")
        db.row_factory = sqlite3.Row
        query = "SELECT ID,pw FROM USERS WHERE ID = ? and pw=?"
        value=(request.form['uid'],request.form['pw'])
        data=db.execute(query,value).fetchall()
        db.close()
        if data:
            flash('이미 존재하는 ID입니다.')
            return redirect(url_for('user_login'))
        else:
            db = sqlite3.connect("DB_project_data.db")
            db.row_factory = sqlite3.Row
            u=db.execute("SELECT count(*)+1 as count from USERS").fetchall()
            db.close()

            db = sqlite3.connect("DB_project_data.db") 
            db.row_factory = sqlite3.Row
            db.execute("INSERT INTO USERS(uID, ID,pw,uName) values( ?,?,?,?)",(u,request.form['uid'],request.form['pw'],request.form['Name']))
            db.commit()
            db.close()
            return redirect(url_for('user_login'))




if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
