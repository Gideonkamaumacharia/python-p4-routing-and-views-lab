#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_route():
    return'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param, end='\n')
    return param

@app.route('/count/<int:param>')
def count_route(param):
    results = ''
    for num in range(0, param):
        results += str(num) + '\n'
    return results

@app.route('/math/<num1>/<opertaion>/<num2>')
def math_route(num1,operation,num2):
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
