from main import app, cursor, conn
from models import query_request, nicknames
from flask import request, jsonify, redirect


dData = {}
lData = []

#creamos index
@app.route('/')
def index(name=''):
    index = {"Welcome": "This is the FenixCMS API"}
    return jsonify(index)

#usuarios
@app.route('/users')
def users():
    data = query_request("SELECT * FROM plan_users LIMIT 0,100", "GET")
    for registro in data:
        dData = {"id":registro[0],"uuid":registro[1],"name":registro[3]}
        lData.append(dData)

    return jsonify(lData)

@app.route('/users/<string:user>')
def single_users(user):
    if user == '':
        return redirect('index')
    data = query_request("SELECT * FROM plan_users WHERE name='%s'" % (user), "GET")
    for registro in data:
        dData = {"id":registro[0],"uuid":registro[1],"name":registro[3],"nicknames":nicknames(registro[1])}
        lData.append(dData)

    return jsonify(lData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
