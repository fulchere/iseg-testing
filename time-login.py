import datetime
import websocket
from websocket import create_connection
import sys
print "python version: %s" % sys.version

ws = create_connection("ws://192.168.1.101:8080",timeout=40)
login = '''{"i":"","t":"login","c":{"l":"user","p":"user","t":""},"r":"websocket"}'''

logins = 600
before = datetime.datetime.now()
for i in range(logins):
    ws.send(login)
    result = ws.recv()
    assert result is not None

after = datetime.datetime.now()
hz = (logins,logins/float(str(after-before)[-9:]))
print "%d requests at %f hz" % hz
print "greater than 10 hz " + u'\u2713' if hz > 10 else "less than 10 hz x"

ws.close()

