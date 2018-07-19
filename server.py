from bottle import route, run

@route('/<input_line>')
def index(input_line):
    return input_line

run(host = 'localhost', port=5533)