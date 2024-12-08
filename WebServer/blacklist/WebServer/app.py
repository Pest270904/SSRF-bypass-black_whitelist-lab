from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
@app.route('/', methods=['POST'])
def home():
    url = request.json.get('url', '')
    for a in ['localhost', '127.0.0.1']:
        if a in url:
            return f"{a} is not allowed";
    return requests.get(url).text