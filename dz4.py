import requests
import string
import random
from flask import Flask, request

app = Flask(__name__)


@app.route('/whoami')
def whoami():
    q1 = request.headers.get('User-Agent', 'None')
    q2 = request.remote_addr
    res = requests.get(f'http://{q2}:8080/whoami')
    q3 = res.headers.get('Date')
    print(q3)
    return f'Browser: {q1}, Ip: {q2},Date: {q3}'


@app.route('/source_code')
def source_code():
    q2 = request.remote_addr
    resp = requests.get(f'http://{q2}:8080/source_code')
    print(resp.text)
    return 'TEXT-TEXT-TEXT-TEXT-TEXT-TEXT-TEXT-TEXT-TEXT-TEXT'


@app.route('/random/<int:length>/<int:specials>/<int:digits>')
def random_url(length, specials, digits):
    if length < 101 and specials & digits == 1:
        print(random.choices(string.ascii_letters + string.punctuation + string.digits, k=length))
    elif length < 101 and specials == 1:
        print(random.choices(string.ascii_letters + string.punctuation, k=length))
    elif length < 101 and digits == 1:
        print(random.choices(string.ascii_letters + string.digits, k=length))
    elif length < 101 and specials & digits != 1:
        print(random.choices(string.ascii_letters, k=length))
    else:
        print('ERROR')
    return 'hi!'


app.run(host="0.0.0.0", port=8080, debug=True)
