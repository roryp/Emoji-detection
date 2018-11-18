from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent import wsgi

from index import *

from scoreText import *

import json

app = Flask(__name__)

emojiList = {
    1  : u'\U0001f602',
    2  : u'\U0001f612',
    3  : u'\U0001f629',
    4  : u'\U0001f62d',
    5  : u'\U0001f60d',
    6  : u'\U0001f614',
    7  : u'\U0001f44c',
    8  : u'\U0001f60a',
    9  : u'\u2764',
    10 : u'\U0001f60f',
    11 : u'\U0001f601',
    12 : u'\U0001f3b6',
    13 : u'\U0001f633',
    14 : u'\U0001f4af',
    15 : u'\U0001f634',
    16 : u'\U0001f60c',
    17 : u'\u263a',
    18 : u'\U0001f64c',
    19 : u'\U0001f495',
    20 : u'\U0001f611',
    21 : u'\U0001f605',
    22 : u'\U0001f64f',
    23 : u'\U0001f615',
    24 : u'\U0001f618',
    25 : u'\u2665',
    26 : u'\U0001f610',
    27 : u'\U0001f481',
    28 : u'\U0001f61e',
    29 : u'\U0001f648',
    30 : u'\U0001f62b',
    31 : u'\u270c',
    32 : u'\U0001f60e',
    33 : u'\U0001f621',
    34 : u'\U0001f44d',
    35 : u'\U0001f622',
    36 : u'\U0001f62a',
    37 : u'\U0001f60b',
    38 : u'\U0001f624',
    39 : u'\u270b',
    40 : u'\U0001f637',
    41 : u'\U0001f44f',
    42 : u'\U0001f440',
    43 : u'\U0001f52b',
    44 : u'\U0001f623',
    45 : u'\U0001f608',
    46 : u'\U0001f613',
    47 : u'\U0001f494',
    48 : u'\u2661',
    49 : u'\U0001f3a7',
    50 : u'\U0001f64a',
    51 : u'\U0001f609',
    52 : u'\U0001f480',
    53 : u'\U0001f616',
    54 : u'\U0001f604',
    55 : u'\U0001f61c',
    56 : u'\U0001f620',
    57 : u'\U0001f645',
    58 : u'\U0001f4aa',
    59 : u'\U0001f44a',
    60 : u'\U0001f49c',
    61 : u'\U0001f496',
    62 : u'\U0001f499',
    63 : u'\U0001f62c',
    64 : u'\u2728'
}

@app.route("/<strings>")
def main(strings):
    
    result = score(strings)
    top5 = result[0]['top5']
    l = map(lambda x: emojiList[x+1], top5.tolist());

    return json.dumps(l, ensure_ascii=False)

@app.route("/x/<strings>")
def hello(strings):
    event = {
        'input': strings
    }
    context = object()
    result = handler(event, context)

    return json.dumps(result, ensure_ascii=False)

SERVER = wsgi.WSGIServer(('127.0.0.1', 5000), app)
SERVER = wsgi.WSGIServer(('0.0.0.0', 5000), app)
SERVER.serve_forever()