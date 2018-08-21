from flask import Flask, request, jsonify
from flask_cors import CORS

from request_gRPC_server import *

app = Flask(__name__)

CORS(app)


@app.route('/acquire')
def acquire():
	"""
	Access to resources
	"""
	duration = int(request.args.get('d'))
	file_name = request.args.get('f')
	response = smple_command_acquire(duration, file_name)
	return jsonify(response)


@app.route('/init')
def init():
	"""
	Initialize device
	"""
	destination = int(request.args.get('d'))
	payload = int(request.args.get('p'))
	response = smple_command_send('INIT', destination, payload)
	return jsonify(response)


@app.route('/ping')
def ping():
	"""
	Connection test
	"""
	destination = int(request.args.get('d'))
	payload = int(request.args.get('p'))
	response = smple_command_send('PING', destination, payload)
	return jsonify(response)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
