#-*- coding:utf-8 -*-
from flask import Flask,request,session,jsonify,url_for,redirect
from flask.templating import render_template

from storage import table

import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    #USERNAME='admin',
    #PASSWORD='qwerty'
    DICR_USERS={'admin1':'qwerty1','admin2':'qwerty2','admin3':'qwerty3'},
    USER_SOLE={'admin1':'true','admin2':'true','admin3':'true'}
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

user='admin'

@app.route('/',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if not app.config['DICR_USERS'].has_key(request.form['username']):
            error='Invalid username'
        elif app.config['USER_SOLE'][request.form['username']]=='false':
            error='此账号已在其他设备登录'
        elif request.form['password']!=app.config['DICR_USERS'][request.form['username']]:
            error='Invalid password'
        else:
            session['logged_in']=True
            app.config['USER_SOLE'][request.form['username']]='false'
            user=request.form['username']
            return redirect(url_for('index'))
    return render_template('login.html',error=error)
    
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    app.config['USER_SOLE'][user]='true'
    return redirect(url_for('login'))
    
@app.route('/display')
def index():
    return render_template('index.html')


@app.route('/get_vars', methods=['GET', 'POST'])
def get_vars():
    print 'called'
    return jsonify(table.extract())

if __name__ == '__main__':
    app.run()
