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
#st = json.loads(json_data)


ws.send(login)


res = ws.recv()
print(res)
ws.close()

