import requests
r = requests.get('http://192.168.1.101/api/login/user/user')
print(r.content)
print(r.text)
print(r.status_code)

import websocket
from websocket import create_connection
#ws = websocket.WebSocket()
#ws.connect("ws://ics.iseg-hv.com:8080", http_proxy_host="proxy_host_name", http_proxy_port=3128)

ws = create_connection("ws://ics.iseg-hv.com:8080")
import json

json_data = '''{
	"i": "",
	"t": "login",
	"c": {
		"l": "admin",
		"p": "password",
		"t": ""
	},
	"r": "websocket"
}'''
st = json.loads(json_data)
print(st)
ws.send(st)
res = ws.recv()
print(res)
ws.close()
