import requests
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

domain = 'http://127.0.0.1:8888/'


def test_acquire():
	path = 'acquire/?d=11&f=11'
	assertion_code(path)


def test_ping():
	path = 'ping/?d=11&p=11'
	assertion_code(path)


def test_init():
	path = 'init/?d=11&p=11'
	assertion_code(path)


def assertion_code(path):
	url = domain + path
	res = requests.get(url)

	assert res.status_code == 200
	assert res.headers["Content-Type"] == "application/json"

	res = res.json()
	assert res[0] == True
	assert res[1] == ''


if __name__ == '__main__':
	if is_running_under_teamcity():
		runner = TeamcityTestRunner()
	else:
		runner = unittest.TextTestRunner()
	unittest.main(testRunner=runner)
