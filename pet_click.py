import click
from request_gRPC_server import *


@click.group()
def pet():
	pass


@pet.command()
@click.argument('ip_port', default='192.168.1.151:40001')
@click.option('-d', '--duration', type=int, help='duration')
@click.option('-f', '--file_name', type=str, help='file_name')
def acquire(ip_port, duration, file_name):
	"""
	Access to resources
	"""
	response = smple_command_acquire(duration, file_name, ip_port)
	print(response)


@pet.command()
@click.argument('ip_port', default='192.168.1.151:40001')
@click.option('-d', '--destination', type=int, help='destination.')
@click.option('-p', '--payload', type=int, help='payload')
def init(ip_port, destination, payload):
	"""
	Initialize device
	"""
	response = smple_command_send('INIT', destination, payload, ip_port)
	print(response)


@pet.command()
@click.argument('ip_port', default='192.168.1.151:40001')
@click.option('-d', '--destination', type=int, help='destination.')
@click.option('-p', '--payload', type=int, help='payload')
def ping(ip_port, destination, payload):
	"""
	Connection test
	"""
	response = smple_command_send('PING', destination, payload, ip_port)
	print(response)


if __name__ == '__main__':
	pet()
