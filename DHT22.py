import Adafruit_DHT as dht

for x in range(100):
	h,t = dht.read_retry(dht.DHT22, 4)
	print 'Temp={0:0.2f}*C  Humidity={1:0.1f}%'.format(t, h)
else:
	print("Done")