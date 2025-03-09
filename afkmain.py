import tkinter as tk
import time
import random
import threading
import psutil
from pynput.keyboard import Key, Controller
from pathlib import Path

buttonText = ["off","on"]
buttonColor = ["#ff0000","#00ff00"]
buttonState = 0
running = False  
keyboard = Controller()

root = tk.Tk()

var1 = tk.IntVar()

root.geometry("320x240")
root.title("AFK SYSTEM")

def is_program_running(programName):
    if programName == "":
        return True
    for process in psutil.process_iter(['name']):
        if process.info['name'] and programName in process.info['name'].lower():
            return True
    return False

def afk():
    global running
    wsad = "wsad"
    programName = TextBox.get("1.0", "end-1c")

    #save program name to file
    file = open("save.txt", "w")
    file.write(programName)
    file.close()

    while running:
        if(not is_program_running(programName)):
            afk_stop()
            break
        index = random.randint(0, 3)
        press_time = random.random() * 0.1
        interval_time = random.random() * 5
        time.sleep(interval_time)
        #print(f"Interval: {interval_time}s | Key: {wsad[index]} | Press: {press_time}s")
        keyboard.press(wsad[index])
        time.sleep(press_time)
        keyboard.release(wsad[index])
        

def afk_stop():
    global buttonState, running
    buttonState = not buttonState
    StartButton.config(text=buttonText[buttonState], fg=buttonColor[buttonState])
    running = bool(buttonState)

def button_click():
    global buttonState, running
    buttonState = not buttonState
    StartButton.config(text=buttonText[buttonState], fg=buttonColor[buttonState])
    running = bool(buttonState)

    if running:
        thread1 = threading.Thread(target=afk, daemon=True)
        thread1.start()

def switch_block_of_text_box():
    if not var1.get():
        TextBox.config(state=tk.DISABLED)
    else:
        TextBox.config(state=tk.NORMAL)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

afkLabel = tk.Label(root, text="AFK")
targetLabel = tk.Label(root, text="Target:")
StartButton = tk.Button(root, text=buttonText[buttonState], command=button_click, fg=buttonColor[buttonState],padx = 100, pady = 50)
TextBox = tk.Text(root,state=tk.DISABLED)
checkBox = tk.Checkbutton(root, text="block textBox",variable=var1, onvalue=0, offvalue=1, command=switch_block_of_text_box)

afkLabel.grid(row = 0, column= 1)
StartButton.grid(row = 1, column= 1)
targetLabel.grid(row = 2, column= 1)
checkBox.grid(row = 3, column=1)
TextBox.grid(row = 4, column=1)


#check if there is a saved target
saved_target = "debil"
if Path("save.txt").is_file():
    file = open("save.txt", "r")
    saved_target = file.read()
else:
    file = open("save.txt","w")
file.close()

TextBox.insert(tk.END, saved_target)

root.mainloop()
