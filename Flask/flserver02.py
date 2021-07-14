from flask import Flask, render_template, request
import MySQLdb as mysql

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #최초 접속
def index():
    db = mysql.connect('localhost', 'root', '12345', 'test', charset = 'utf8')
    cur = db.cursor(mysql.cursors.DictCursor)
    cur.execute('SELECT * FROM student')
    reusult = []
    while True:
        student = cur.fetchone()
        if not student: break

        reusult.append(student) #리스트 추가

    cur.close()
    db.close()
    #백엔드에서 테이터를 프론트엔드로 전달        
    return render_template('mysqldata.html', row=reusult)

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=8080, debug=True)