import requests
#r = requests.get('http://192.168.1.101/api/login/user/user')
#print(r.content, r.text, r.status_code) ### HTTP doesn't work with this power supply

import websocket
from websocket import create_connection
#ws = websocket.WebSocket()
#ws.connect("ws://192.168.1.101:8080", http_proxy_host="proxy_host_name", http_proxy_port=3128)

ws = create_connection("ws://192.168.1.101:8080")
import json

login = '''{"i":"","t":"login","c":{"l":"user","p":"user","t":""},"r":"websocket"}'''
ws.send(login)
res = ws.recv()
print(res)


getVoltage = '''{
	"i": "55005e1a49cad-23",
	"t": "request",
	"c": [
		{
			"c": "getItem",
			"p": {
				"p": {
					"l": "0",
					"a": "*",
					"c": "*"
				},
				"i": "Status.firmwareRelease",
				"v": "",
				"u": ""
			}
		}
	],
	"r": "websocket"
}'''
ws.send(getVoltage)
res2 = ws.recv()
print(res2)
res2 = ws.recv()
print(res2)


ws.close()

