from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return {'Key': 'value'}

run(app, host='localhost', port=8080, debug=True)
