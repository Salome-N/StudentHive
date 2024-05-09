from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def app_status():
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)