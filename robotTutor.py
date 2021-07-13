
from tkinter import *
from tkinter import ttk
import webbrowser
from serial.tools import list_ports
import serial
    
root = Tk()


#application title and instruction text
title = ttk.Label(root, text = "RobotTutor.tech")
title.config(font = ('Courier', 32, 'bold'), background = 'yellow')
title.pack(pady = 20)

text = ttk.Label(root, text = "Connect your robot via Bluetooth to this computer. From the droupdown list, select the COM port on the computer that the robot is connected to. Click 'connect robot' to open the robot programming application on your web browser. A beep sound on the robot indicates that it is ready for use :) ")
text.config(wraplength = 800)
text.pack(pady = 20)


#select com port
label1 = ttk.Label(root, text = "Select COM port")
label1.config(font = ('Courier', 18 ,'bold'), foreground = 'blue')
label1.pack(pady = 20)

OPTIONS = serial.tools.list_ports.comports(include_links=False)

comPorts = StringVar(root)
cutOptions = []

for comPorts in OPTIONS:
    cutOptions.append(comPorts.device)

print (cutOptions)
comPorts.set(cutOptions[0]) # default value displayed on the menu

dropdownMenu = OptionMenu(root, comPorts, *cutOptions)
dropdownMenu.pack()


#connect robot
button = ttk.Button(root, text = "Connect Robot")
button.pack(pady = 20)

def connectRobot():
    port = comPorts.get()

    print (port)
    
    portLen = len(port)
    shortPort = ""

    for i in range(0, portLen-6):
        shortPort = shortPort + port[i]

    print (shortPort)
    
    ser = serial.Serial(port, 9600)
    data = "PlayNote 100,100\n"
    ser.write(data.encode())
    
    webbrowser.open("http://robottutor.tech/")

button.config(command = connectRobot)  

root.mainloop()

#'/dev/tty.FA103962-Port'
