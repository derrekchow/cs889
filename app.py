from flask import Flask, url_for, render_template, request, jsonify
from script_v1 import words_list, add

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    w1 = request.values.get('w1')
    w2 = request.values.get('w2')
    if (w1 is not None and w2 is not None):
        return jsonify(add(int(w1), int(w2)))
    else:
        return render_template('index.html', data=words_list)
    