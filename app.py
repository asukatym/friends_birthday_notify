from flask import Flask, g, request                                                                                               
import sqlite3
import json 

app = Flask(__name__)
              
def get_db():#データベースのコネクションを取得
    dbname = 'birthday.db'
    con = sqlite3.connect(dbname)
    con.text_factory = lambda b: b.decode(errors = 'ignore')
     
              
@app.route('/birthday', methods=['GET'])
def get_birthday():
    dbname = 'birthday.db'
    con = sqlite3.connect(dbname)
    con.row_factory = sqlite3.Row #カラム名取得
    cur = con.cursor() #カーソル取得
              
    cur.execute('SELECT * FROM birthday_list')
    data = []
    for row in cur.fetchall(): #sqlite3.Row オブジェクトを dict に変換
        data.append(dict(row))
              
    return json.dumps(data,indent=2)

if __name__ == "__main__":
    app.run()
 


