from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    operation = request.form['operation']

    if operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        result = number1 / number2

    return render_template('result.html', result=result)




if __name__ == '__main__':
    app.run(debug=True)
