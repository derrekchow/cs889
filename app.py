from flask import Flask, url_for, render_template, request, jsonify
from script import word_dict, add

app = Flask(__name__)

@app.route('/')
def index():
    w1 = request.values.get('w1')
    w2 = request.values.get('w2')
    if (w1 is not None and w2 is not None):
        return jsonify(add(int(w1), int(w2)))
    else:
        data = { 'words' : word_dict }
        return render_template('index.html', data=data)

@app.route('/search')
def login(): pass

@app.route('/user/')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('index', _external=True))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Tutorials Point'))
