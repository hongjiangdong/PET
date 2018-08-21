import grpc
import petdriver_pb2
import petdriver_pb2_grpc

default_ip_port = '192.168.1.151:40001'


def smple_command_acquire(duration, file_name, ip_port=default_ip_port):
	channel = grpc.insecure_channel(ip_port)
	stub = petdriver_pb2_grpc.PetDriverStub(channel)
	response = stub.AcquireData(petdriver_pb2.AcqParam(duration=duration, file_name=file_name))
	return response.result, response.err_msg


def smple_command_send(enum, d, p, ip_port=default_ip_port):
	channel = grpc.insecure_channel(ip_port)
	stub = petdriver_pb2_grpc.PetDriverStub(channel)
	response = stub.SendCommand(petdriver_pb2.Command(cmd=enum, dst=d, payload=p))
	return response.result, response.err_msg
