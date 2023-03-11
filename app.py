# Put your app in here.

from flask import Flask, request

app = Flask(__name__)

@app.rout('/add')
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = add(a, b)
    return f'{result}'


@app.rout('/sub')
def sub():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = add(a, b)
    return f'{result}'


@app.rout('/mult')
def mult():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = add(a, b)
    return f'{result}'


@app.rout('/div')
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = add(a, b)
    return f'{result}'