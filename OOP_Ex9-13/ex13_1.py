from flask import Flask

app = Flask(__name__)


@app.route('/')
def redirect():
    return 'Click the <a href=/prime_number/>link</a> to evaluate your number.'


@app.route('/prime_number/')
def enter_prime():
    return 'Please enter a number in the end of URL to test.'


@app.route('/prime_number/<num>', methods=['GET'])
def test_prime(num):
    prime = True
    num = int(num)
    if num <= 1:
        return "Entered number should be greater than 1"
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        return {"Number": num, "isPrime": prime}


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
