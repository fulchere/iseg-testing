import datetime
import websocket
from websocket import create_connection
import sys
print "python version: %s" % sys.version

ws = create_connection("ws://192.168.1.101:8080",timeout=40)
login = '''{"i":"","t":"login","c":{"l":"user","p":"user","t":""},"r":"websocket"}'''

ls = []
logins = 300
before = datetime.datetime.now()
for i in range(logins):
    ws.send(login)
    result = ws.recv()
    ls.append(result)

#print(ls)
after = datetime.datetime.now()
print "%d requests at %f hz" % (logins,logins/float(str(after-before)[-9:]))
ws.close()

