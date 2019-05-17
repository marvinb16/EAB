from tkinter import *
import Adafruit_DHT as dht

root = Tk()

def getDHT():
    h, t = dht.read_retry(dht.DHT22, 4)
    print('Temp={0:0.2f}*C  Humidity={1:0.1f}%'.format(t, h))

button1 = Button(root, text="Get Stats", command=getDHT)
root.mainloop()