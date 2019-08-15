import json
import time
import threading
from websocket import create_connection

ws = create_connection("ws://192.168.1.101:8080",timeout=40)

login_request = '''{
	"i": "",
	"t": "login",
	"c": {
		"l": "user",
		"p": "user",
		"t": ""
	},
	"r": "websocket"
}'''
ws.send(login_request)
login_message = ws.recv()
session_id = json.loads(login_message)['i']
getVoltage= '''{
	        "i": "%s",
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
            }''' % session_id

getConfig = '''{
            "i":"%s",
            "t":"getConfig",
            "c":[],
            "r":"websocket"
            }''' % session_id

ws.send(getVoltage)

def get_json():
    while True:
        received = ws.recv()
        jsoned = json.loads(received)
        print(json.dumps(jsoned, indent=4, sort_keys=True))
        if 'c' in jsoned[0]:
            for item in jsoned[0]['c']:
                typ = item['d']['i']
                if typ == "System.time":
                    print("TIME:",item['d']['v'])
                if typ == "Status.temperature0":
                    print("TEMP0",item['d']['v'],item['d']['u'])
                if typ == "Status.temperature1":
                    print("TEMP1:",item['d']['v'],item['d']['u'])
                if typ == "Status.voltageMeasure":
                    print("VOLTAGE:",item['d']['v'],"CHANNEL:",item['d']['p']['c'],item['d']['u'])
                if typ == "Status.currentMeasure":
                    print("CURRENT:",item['d']['v'],"CHANNEL:",item['d']['p']['c'],item['d']['u'])
                if typ == "Status.safetyLoopClosed":
                    print("LOOP STATUS: (1=True,0=False)",item['d']['v'])
t_ls = []
for i in range(2):
    thrd = threading.Thread(target=get_json)
    t_ls.append(thrd)
for t in t_ls:
    t.start()
for t in t_ls:
    t.join()

ws.close()

