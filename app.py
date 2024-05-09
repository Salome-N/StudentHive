from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def app_status():
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)