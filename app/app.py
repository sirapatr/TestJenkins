from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my simple-API"

@app.route('/getcode', methods=['GET'])
def getCode():
    return "Fission"

@app.route('/plus/<num1>/<num2>', methods=['GET'])
def plus(num1, num2):
    try:
        num1 = eval(num1)
        num2 = eval(num2)
    except:
        return jsonify({'message' : 'Inputs must be numbers'}), 400
    return jsonify({'result': num1 + num2}), 200

if __name__ == '__main__':
    app.run()