import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Приложение'


if __name__ == '__main__':
    port = int(os.environ.get('port', 5000))
    app.run(port=port, host='0.0.0.0')
