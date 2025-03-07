from flask import Flask, render_template, jsonify, request
from functions import get_answer

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['message']
    bot_answer = get_answer(user_input)
    return jsonify({"reply":bot_answer})

if __name__ == '__main__':
    app.run(debug=True)