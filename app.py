from flask import Flask, jsonify, render_template
from auth import auth_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/')
def main():
    return 'main'

@app.route('/index')
def index():
    return 'index'

@app.route('/hello_<name>')
def hello_name(name:str):
    return render_template('hello.html', name=name)

@app.route('/json')
def json():
    return jsonify({"message": "Test"})

if __name__ == '__main__':
    app.run(debug=True)