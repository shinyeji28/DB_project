from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3 
import sys

app = Flask(__name__)
app.secret_key = 'abcd'

USER_NAME="qw"

@app.route('/')
def first_page():    
    return render_template('first.html')

@app.route('/login',methods=['GET','POST'])
def user_login():
    return render_template('login.html')

@app.route('/<string:ID>/exhib', methods=['GET','POST'])
def showexhib(ID):
    db = sqlite3.connect("DB_project_data.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select * from EXHIBITION'
    ).fetchall()
    db.close()
    return render_template('context.html',items=items,ID2 = ID)

@app.route('/exhib/edit', methods=['GET','POST'])
def editMenu():
    if request.method=='POST':
        db = sqlite3.connect("DB_project_data.db")
        db.row_factory = sqlite3.Row
        query = "SELECT ID,pw,uName FROM USERS WHERE ID = ? and pw=?"
        value=(request.form['uid'],request.form['pw'])
        data=db.execute(query,value).fetchall()
        db.close()

        if data:
            return redirect(url_for('showexhib',ID=request.form['uid']))
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
            db.execute('INSERT INTO USERS(ID,pw,uName,birthday, phoneNumber, eMail) values(?,?,?,?,?,?)'
                    ,(request.form['uid'],request.form['pw'],request.form['Name'],request.form['birth'],request.form['phone'],request.form['email']))
            db.commit()
            db.close()
            return redirect(url_for('showexhib',ID=request.form['uid']))

@app.route('/detail_information/<int:e>/<string:ID3>', methods=['GET', 'POST'])
def detail_info(e,ID3):
    db = sqlite3.connect("DB_project_data.db")
    db.row_factory = sqlite3.Row
    item = db.execute(
        'select * from EXHIBITION where eID=?',(e,)
    ).fetchall()
    data=db.execute('select cName,content from COMMENT where eID=?',(e,)).fetchall()
    db.close()
    return render_template('detail.html',items=item,ID4=ID3,datas=data)


@app.route('/comment/<int:eID>/<string:ID5>', methods=['GET', 'POST'])
def comment(eID,ID5):
    db = sqlite3.connect("DB_project_data.db")
    c=db.cursor()
    data=c.execute('select count(*)+1 from COMMENT').fetchone()

    for r in data:
        db.execute("INSERT INTO COMMENT(cID,cName,content,eID) values(?,?,?,?)",(r, ID5,request.form['user_message'],eID))
    db.commit() 
    db.close()
    return redirect(url_for('detail_info',e=eID,ID3=ID5))


@app.route('/reserve/<string:ID6>/<int:e>' , methods=['GET','POST'])
def reserve(ID6,e):  
    db = sqlite3.connect("DB_project_data.db")
    db.row_factory = sqlite3.Row
    c=db.cursor()
    d=db.cursor()
    datas=c.execute('select * from USERS where ID=?',(ID6,)).fetchall()
    datas2=d.execute('select childPrice,teenPrice, adultPrice from EXHIBITION where eID=?',(e,)).fetchone()
    a,b,c=datas2
    a=int(float(a))
    b=int(float(b))
    c=int(float(c))
    db.close()
    return render_template('reserve.html',ID7=ID6,userInfo=datas,eID=e,ra=a,rb=b,rc=c)

@app.route('/reserve_accepct/<string:ID8>/<int:e>' , methods=['GET','POST'])
def reserve_accepct(ID8,e):  
    db = sqlite3.connect("DB_project_data.db")
    db.row_factory = sqlite3.Row
    c=db.cursor()
    d=db.cursor()
    datas2=d.execute('select childPrice,teenPrice, adultPrice from EXHIBITION where eID=?',(e,)).fetchone()
    a1,b1,c1=datas2
    a1=int(float(a1))
    b1=int(float(b1))
    c1=int(float(c1))
    cp = int(request.form['child'])*a1
    tp = int(request.form['teen'])*b1
    ap = int(request.form['adult'])*c1
    total = cp+tp+ap
    data=c.execute('select count(*)+1 from RESERVATION').fetchone()
    for r in data:
        db.execute('INSERT INTO RESERVATION(rID,uID,eID,childNum,teenNum,adultNum,delivery,totalPrice) values(?,?,?,?,?,?,?,?)'
        ,(r, ID8,e,request.form['child'],request.form['teen'],request.form['adult'],request.form['ticket'],total))
    db.commit()
    db.close()

    return redirect(url_for('showexhib',ID=ID8))

@app.route('/inquiry/<string:ID9>', methods=['GET','POST'])
def inquiry(ID9):
    db1 = sqlite3.connect("DB_project_data.db")
    db1.row_factory = sqlite3.Row
    c1=db1.cursor()
    data=c1.execute('select * from RESERVATION R, EXHIBITION E where R.eID=E.eID and R.uID=?',(ID9,)).fetchall()
    db1.close()
    
    return render_template('inquiry.html',ID0=ID9,view=data)

    
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)