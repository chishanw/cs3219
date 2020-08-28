import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_number():
    number = random.randint(0, 100)
    return { 'number': number }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
