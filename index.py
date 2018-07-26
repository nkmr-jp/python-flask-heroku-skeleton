import os

from bottle import route, run


@route('/')
def hello_world():
    return os.environ.get('HELLO_MESSAGE', 'hello world')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
