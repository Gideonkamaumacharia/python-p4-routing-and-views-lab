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

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Division by zero is not allowed!'
    elif operation == 'mod':
        result = num1 % num2
    else:
        return 'Invalid operation. Supported operations: add, sub, mul, div, mod'
    
    return f'<h3>Result of {num1} {operation} {num2}:</h3><p>{result}</p>'

if __name__ == '__main__':
    app.run(debug=True)