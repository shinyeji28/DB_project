from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/exhib')
def showexhib():
    db = sqlite3.connect("DB_project_data.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select * from EXHIBITION'
    ).fetchall()
    db.close()
    return render_template('context.html',items=items)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        db = sqlite3.connect("DB_project_data.db")
        db.row_factory = sqlite3.Row
        query = "SELECT ID FROM USERS WHERE ID = ?"
        value=(request.form['uid'],request.form['pw'])
        data=db.execute(query,value).fetchall()

        db.close()
        if data:
           print 'login success'
           return redirect(url_for('showexhib'))

        else:
            # 팝업창
    
 
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)