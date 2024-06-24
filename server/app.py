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
    for num in range(1, param + 1):
        results += str(num) + '\n'
    return results

if __name__ == '__main__':
    app.run(port=5555, debug=True)
