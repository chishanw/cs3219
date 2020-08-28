from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_number():

    number = int(request.args.get('num'))

    if not number:
        number = 0

    is_low = number < 51
    is_high = number > 50

    if is_low:
        message = 'This is a pretty low number.'

    if is_high:
        message = 'This is a fairly high number.'


    return { 'message': message }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')