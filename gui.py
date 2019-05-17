from tkinter import *
#import Adafruit_DHT as dht

root = Tk()
root.title('Plant Monitor')

root.geometry("500x500")
root.resizable(0, 0)

def getDHT():
#    h, t = dht.read_retry(dht.DHT22, 4)
    print('Temp={0:0.2f}*C  Humidity={1:0.1f}%')

menu = Menu(root)
root.config(menu=menu)
# DropDown menu Config
# menuname = Menu("the frame", tearoff=0
# menu.add_cascade(label, menu=^^)
# men

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Load Datalog", command=getDHT)
subMenu.add_command(label="Fuck shit up", command=getDHT)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=getDHT)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="fuck")

# toolbar :)
toolbar = Frame(root, bg="blue")

readTemp = Button(toolbar, text="Temp", command=getDHT)
readTemp.pack(side=LEFT, padx=6, pady=6)
readHud  = Button(toolbar, text="Humidity", command=getDHT)
readHud.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status Bar

status = Label(root, text="Shitman", bd=2, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# graphics

canvas = Canvas(root)
canvas.pack()

line = canvas.create_line(0,0,200,50)
root.mainloop()