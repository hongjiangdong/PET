import grpc

import petdriver_pb2
import petdriver_pb2_grpc
import click


@click.group()
def pet():
	pass


@pet.command()
@click.argument('ip_port', default='192.168.1.151:40001')
@click.option('-d', '--duration', type=int, help='duration')
@click.option('-f', '--file_name', type=str, help='file_name')
def acquire(ip_port, duration, file_name):
	# NOTE(gRPC Python Team): .close() is possible on a channel and should be
	# used in circumstances in which the with statement does not fit the needs
	# of the code.
	response = smple_command_acquire(ip_port, duration, file_name)
	print(response)


def smple_command_acquire(ip_port, duration, file_name):
	with grpc.insecure_channel(ip_port) as channel:
		stub = petdriver_pb2_grpc.PetDriverStub(channel)

		response = stub.AcquireData(petdriver_pb2.AcqParam(duration=duration, file_name=file_name))
		return response.result, response.err_msg


@pet.command()
@click.argument('ip_port', default='192.168.1.151:40001')
@click.option('-d', '--destination', type=int, help='destination.')
@click.option('-p', '--payload', type=int, help='payload')
def init(ip_port, destination, payload):
	"""
	Initialize device
	"""
	response = smple_command_send(ip_port, 'INIT', destination, payload)
	print(response)


@pet.command()
@click.argument('ip_port', default='192.168.1.151:40001')
@click.option('-d', '--destination', type=int, help='destination.')
@click.option('-p', '--payload', type=int, help='payload')
def ping(ip_port, destination, payload):
	response = smple_command_send(ip_port, 'PING', destination, payload)
	print(response)


def smple_command_send(ip_port, enum, d, p):
	with grpc.insecure_channel(ip_port) as channel:
		stub = petdriver_pb2_grpc.PetDriverStub(channel)
		response = stub.SendCommand(
			petdriver_pb2.Command(cmd=enum, dst=d, payload=p))
		# petdriver_pb2._COMMAND_CMD.values_by_name[enum].index
		return response.result, response.err_msg


if __name__ == '__main__':
	pet()
