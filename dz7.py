import string
import random
import time
from html import escape
from flask import Flask, request

app = Flask(__name__)


def css_whoami():
    return """body {
           background: linear-gradient(45deg, #1FA2FF, #12D8FA, #A6FFCB);
        }
        .next {
            font-weight: 600;
            color: #ffe484;
        }
        .next:hover {
            background: #ffe484;
            text-decoration: none;
        }
        .python{
            text-align: right
        }
        .vf1 {
            width:1150px;
            border-top: solid 2px #E9D87C;
        }
        .vf2 {
            width:1150px;
            border-top: solid 2px #E9D87C;
        }
        .vf3 {
            width:1150px;
            border-top: solid 2px #E9D87C;
            border-bottom: solid 2px #E9D87C;
        }
    """


def css_source_code():
    return """body {
           background: linear-gradient(45deg, #1FA2FF, #12D8FA, #A6FFCB);
        }
        .next {
            text-align: right;
            font-weight: 600;
            color: #ffe484;
        }
        .back {
            text-align: right;
            font-weight: 600;
            color: #8b00ff;
        }
        .next:hover {
            background: #ffe484;
            text-decoration: none;
        }
        .python {
            text-align: right
        }
        .back:hover {
            background: #8b00ff;
            text-decoration: none;
        }
        .download {
             background: linear-gradient(45deg, #1FA2FF, #12D8FA, #A6FFCB);
        }
        """


def css_random():
    return """body {
           background: linear-gradient(45deg, #1FA2FF, #12D8FA, #A6FFCB);
        }
        .back {
            text-align: right;
            font-weight: 600;
            color: #8b00ff;
        }
        .back:hover {
            background: #8b00ff;
            text-decoration: none;
        }
        .python {
            text-align: right
        }
        .reload {
            background: linear-gradient(45deg, #1FA2FF, #12D8FA, #A6FFCB);
        }
        """


@app.route('/whoami')
def whoami():
    q1 = request.headers.get('User-Agent', 'None')
    q2 = request.remote_addr
    q3 = time.strftime('%A %B, %d %Y %H:%M:%S')
    return f"""
    <html>
        <head>
        <title>Whoami</title>   
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
         <style>
        {css_whoami()}
       </style>
        </head>
        <body>
        <a class='next' href='/source_code'> Next</a>
        <br>
        <img src='https://s.dou.ua/img/events/Python-logo-notext.svg_Mq7wlhT.png' align='right' width='150' height='150'>
        <li class='vf1'>{q1}</li>
        <br>
        <li class='vf2'>{q2}</li>
        <br>
        <li class='vf3'>{q3}</li>
        </body> 
    </html>
    """


@app.route('/source_code')
def source_code():
    with open(__file__, 'r') as f:
        file = f.readlines()
    code = escape("".join(file))

    return f"""
    <html>
        <head>
        <title>Source code</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <img src='https://s.dou.ua/img/events/Python-logo-notext.svg_Mq7wlhT.png' align='right' width='150' height='150'>
        <style>
        {css_source_code()}
       </style>
        </head>
        <body>
        <a class='back' href='/whoami'> Back</a>
        <a class='next' href='random/10/0/0'> Next</a>
        <br>
        <a href="#" download="" align: right>
            <button class='download'>Download </button></a>
        <pre>{code}</pre>

        </body>
    </html>
    """


@app.route('/random/<int:length>/<int:specials>/<int:digits>')
def random_url(length, specials, digits):
    global v
    if length < 101 and specials & digits == 1:
        v = random.choices(string.ascii_letters + string.punctuation + string.digits, k=length)
    elif length < 101 and specials == 1:
        v = random.choices(string.ascii_letters + string.punctuation, k=length)
    elif length < 101 and digits == 1:
        v = random.choices(string.ascii_letters + string.digits, k=length)
    elif length < 101 and specials & digits != 1:
        v = random.choices(string.ascii_letters, k=length)
    else:
        v = 'ERROR'
    return f"""
    <html>
        <head>
        <title>Random</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <img src='https://s.dou.ua/img/events/Python-logo-notext.svg_Mq7wlhT.png' align='right' width='150' height='150'>
        <style>
        {css_random()}
       </style>
        </head>
        <body>
        <a class='back' href='/source_code'> Back</a>
        <br>
        <h4>Result: {v}</h4>
        <button class='reload' onclick='window.location.reload(true)'>Refresh the page</button>
        </body>
    </html>
    """


app.run(host="0.0.0.0", port=8080, debug=True)
