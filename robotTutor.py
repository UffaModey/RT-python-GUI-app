from tkinter import *
from tkinter import ttk
import tkinter as tk
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

allComPorts = serial.tools.list_ports.comports(include_links=False)

optionsList = []

for i in allComPorts:
    optionsList.append(i.device)

valueInside = StringVar(root)

print (optionsList)

dropdownMenu = ttk.OptionMenu(root, valueInside, optionsList[0], *optionsList)

dropdownMenu.pack()


#connect robot
button = ttk.Button(root, text = "Connect Robot")
button.pack(pady = 20)

def connectRobot():
    port = valueInside.get()

    print (port)
    
    ser = serial.Serial(port, 9600)
    data = "PlayNote 100,100\n"
    ser.write(data.encode())
    
    webbrowser.open("http://robottutor.tech/")

button.config(command = connectRobot)  

root.mainloop()

#'/dev/tty.FA103962-Port'
