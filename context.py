from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def showMenu():
    db = sqlite3.connect('DB_project_data.db')
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select * from EXHIBITION'
    ).fetchall()
    db.close()
    return render_template('context.html',items=items)

"""     output=""
    for item in items:
        #output += item['eID'] + '<br>'
        output += item['currentORfuture'] + " "
        output += item['place'] + '<br>'
        output += item['eName'] + '<br>'
        output += item['period'] + '<br>'
        output += item['room'] + '<br>'
        output += item['childPrice'] + '<br>'
        output += item['teenPrice'] + '<br>'
        output += item['adultPrice'] + '<br>' """
    


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=5000)