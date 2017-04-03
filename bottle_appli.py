from bottle import route, run
import appliActivites

@route('/hello')
def page():
    return transform_equip()

run(host='localhost', port=8082, debug=True)