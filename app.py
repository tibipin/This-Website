from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(message='Pizza'), 200 # 200 here is the http response status

@app.route('/parameters/<string:name>/<int:age>')
def parameters(name: str, age: int):
    if age < 18: 
        return jsonify(message=f'Sorry, {name}. You are not old enough'), 401
    else:
        return jsonify(message=f'Welcome {name}, you are old enough to see this website')


if __name__ == '__main__':
    app.run(debug=True)
