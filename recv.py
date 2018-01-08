import pymysql.cursors
import serial
import time
import data

def getSerial():
	return serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def connectSQL():
	conn = pymysql.connect(host='bengis.cjgicbekjjvr.us-east-1.rds.amazonaws.com',
                             user='sight',
                             password='ICantSee',
                             db='sight',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
	return conn

def scan(s):
	s.write(b'SCAN')
	time.sleep(0.1)
	read(s)

def sweep(s):
	s.write(b'SWEEP')
	time.sleep(0.1)
	read(s)

def reset(s):
	s.write(b'RESET')
	time.sleep(0.1)
	read(s)

def read(s):
	out = s.readline().decode()
	if len(out) > 5:
		out = out[5:]
	time.sleep(0.1)
	return out.strip()

def clearin(s):
	line = read(s)
	while line != '':
		line = read(s)
		time.sleep(0.1)

def getdistlist(s):
	sweep(s)
	line = read(s)
	outs = []
	while line != '':
		time.sleep(0.05)
		if(line.startswith("ERROR")):
			line = read(s)
			continue
		dstr = line.split("DIST:")
		dist = float(dstr[1])
		outs.append(dist)
		time.sleep(0.1)
		line = read(s)
	return outs

def waitforavail(s):
	avail = 0

	while avail < 5:
		scan(s)
		line = read(s)
		while line != '':
			if(line.startswith("Found Node ")):
				avail += 1
			line = read(s)
			time.sleep(0.1)
		time.sleep(0.5)

conn = connectSQL()
ser = getSerial()
clearin(ser)
data.setGlobals()

waitforavail(ser)

def processAndSendData(conn, dist):
	x, y = data.processData(dist) # -- Connects to Jui's/Ben's module
	with conn.cursor() as cur:
		qu = "INSERT INTO loc(x, y) VALUES (%s, %s);"
		cur.execute(qu, (x, y))
		conn.commit()

while(True):
	fails = 0
	distances = getdistlist(ser)
	print(distances)
	if(len(distances) != 5):
		waitforavail(ser)
		fails += 1
		if fails == 6:
			reset()
			fails = 0
	else:
		processAndSendData(conn, distances)

