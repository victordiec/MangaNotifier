from bottle import route, run

@route('/hello')
def hello():
    return {'Key': 'value'}

run(host='localhost', port=8080, debug=True)
