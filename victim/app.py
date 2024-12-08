from flask import Flask

app = Flask(__name__)

@app.route('/flag')
def flag():
    return "Flag{814ck_4nd_wh1t3_4r3_7h3_8357}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)