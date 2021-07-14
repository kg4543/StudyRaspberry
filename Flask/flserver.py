from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/get', methods = ['GET'])
def get():
    user = request.args.get('user')
    msg = "{0}".format(user)
    return msg

@app.route('/post', methods = ['POST'])
def post():
    userid = request.form.get('userid')
    password = request.form.get('password')
    msg = "{0} / {1}".format(userid, password)
    friends = ['Lee', 'Park', 'Kim']
    return render_template('result.html', result = msg, friends=friends)

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=8080, debug=True)