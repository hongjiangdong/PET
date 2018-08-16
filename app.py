import json

from flask import Flask, request, jsonify
import grpc

import petdriver_pb2
import petdriver_pb2_grpc

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

ip_port = '127.0.0.1:40001'
channel = grpc.insecure_channel(ip_port)


@app.route('/acquire/')
def acquire():
	"""
	Access to resources
	"""
	duration = int(request.args.get('d'))
	file_name = request.args.get('f')
	response = smple_command_acquire(duration, file_name)
	return jsonify(response)


def smple_command_acquire(duration, file_name):
	stub = petdriver_pb2_grpc.PetDriverStub(channel)
	response = stub.AcquireData(petdriver_pb2.AcqParam(duration=duration, file_name=file_name))
	return response.result, response.err_msg


@app.route('/init/')
def init():
	"""
	Initialize device
	"""
	destination = int(request.args.get('d'))
	payload = int(request.args.get('p'))
	response = smple_command_send('INIT', destination, payload)
	return jsonify(response)


@app.route('/ping/')
def ping():
	"""
	Connection test
	"""
	destination = int(request.args.get('d'))
	payload = int(request.args.get('p'))
	response = smple_command_send('PING', destination, payload)
	return jsonify(response)


def smple_command_send(enum, d, p):
	stub = petdriver_pb2_grpc.PetDriverStub(channel)
	response = stub.SendCommand(
		petdriver_pb2.Command(cmd=enum, dst=d, payload=p))
	return response.result, response.err_msg


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
# app.run(debug=True)
