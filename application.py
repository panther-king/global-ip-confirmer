from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def confirm():
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run()
