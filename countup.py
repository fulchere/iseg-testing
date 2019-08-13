import datetime

bf1 = datetime.datetime.now()
num = 10000000
for i in range(num):
    print(i)
af1 = datetime.datetime.now()

bf2 = datetime.datetime.now()
num2 = 10000000
ls = []
for i in range(num):
    ls.append(i)
print ls
af2 = datetime.datetime.now()

print "without container" + str(af1-bf1)[-9:]
print "with    container" + str(af2-bf2)[-9:]
