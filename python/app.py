from flask import Flask, jsonify
import pika

app = Flask(__name__)

@app.route('/product')
def product():
    response = {
        'name': '테스트 이름',
        'price': '테스트 가격',
        'category': '테스트 카테고리'
    }

    return jsonify(response), 200

@app.route('/api')
def test():
    return 'hello test'

@app.route('/')
def home():
    return 'hello test'   

if __name__ == '__main__':
    app.run()
    
    