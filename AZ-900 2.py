
from tkinter import *
from tkinter import ttk
import webbrowser
from serial.tools import list_ports
    
root = Tk()


#application title and instruction text
title = ttk.Label(root, text = "Robottutor.tech")
title.config(font = ('Courier', 32, 'bold'), background = 'yellow')
title.pack(pady = 20)

text = ttk.Label(root, text = "Connect your robot via Bluetooth to this computer. Select the COM port on the computer that the robot is connected to from the dropdown list. Input www.robottutor.tech in the text box. Click connect to open the robot programming application on your web browser. A beep sound on the robot indicates that it is ready for use :) ")
text.config(wraplength = 800)
text.pack(pady = 20)


#select com port
label1 = ttk.Label(root, text = "Select COM port")
label1.config(font = ('Courier', 18 ,'bold'), foreground = 'blue')
label1.pack(pady = 20)

OPTIONS = list_ports.comports()

comPorts = StringVar(root)
comPorts.set(OPTIONS[0]) # default value displayed on the menu

dropdownMenu = OptionMenu(root, comPorts, *OPTIONS)
dropdownMenu.pack()



#input robot programming application URL
label2 = ttk.Label(root, text = "Robot programming application URL")
label2.config(font = ('Courier', 18 ,'bold'), foreground = 'blue')
label2.pack(pady = 20)

appURL = ttk.Entry(root)
URL = appURL.get()
appURL.pack()


#connect robot
button = ttk.Button(root, text = "Connect Robot")
button.pack(pady = 20)

def connectRobot():
    print ("PlayNote 100,100\n") > /dev/tty.FA103962-Port
    webbrowser.open("http://robottutor.tech/")

button.config(command = connectRobot)  

root.mainloop()
