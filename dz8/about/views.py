import random
import string
import time
from django.http import HttpResponse
from html import escape
from django.shortcuts import render


def whoami(request):
    q1 = request.headers.get('User-Agent', 'None')
    q2 = time.strftime('%A %B, %d %Y %H:%M:%S')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(f"""
    <a href='http://127.0.0.1:8000/about/source_code'> Next </a><br>
    {q1}, <br>{ip}, <br>{q2}
""")


def source_code(request):
    with open(__file__, 'r') as f:
        file = f.readlines()
    code = escape("".join(file))
    return HttpResponse(f"""
    <a href='http://127.0.0.1:8000/about/whoami'> Back </a>
    <a href='http://127.0.0.1:8000/about/random/10/0/0'> Next </a>
    <pre>{code}</pre>
""")


def random_url(request, length, specials, digits):
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
    return HttpResponse(f"""
        <a href='http://127.0.0.1:8000/about/source_code/'> Back </a><br>
        {v}
    """)