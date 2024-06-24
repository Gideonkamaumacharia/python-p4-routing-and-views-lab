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
def math(num1,operation,num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation specified!'
    
    return f"Result of {num1} {operation} {num2} is {result}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
