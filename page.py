from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3, sys

app = Flask(__name__)
app.secret_key = 'abcd'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/exhib')
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
        query = "SELECT ID,pw FROM USERS WHERE ID = ? AND pw = ?"
        value=(request.form['uid'],request.form['pw'])
        data=db.execute(query,value).fetchall()
        db.close()
        if data:
            return redirect(url_for('showexhib'))
        else:
            flash('회원 정보가 없습니다.')
            return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)