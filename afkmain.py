import tkinter as tk
from pynput.keyboard import Key, Controller
import time
import random
import threading
import psutil

buttonText = ["off","on"]
buttonColor = ["#ff0000","#00ff00"]
buttonState = 0
running = False  
keyboard = Controller()

root = tk.Tk()

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
    while running:
        if(not is_program_running(programName)):
            afk_stop()
            break
        index = random.randint(0, 3)
        press_time = random.random() * 1.5
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

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

afkLabel = tk.Label(root, text="AFK")
targetLabel = tk.Label(root, text="Target:")
StartButton = tk.Button(root, text=buttonText[buttonState], command=button_click, fg=buttonColor[buttonState],padx = 100, pady = 50)
TextBox = tk.Text(root)

afkLabel.grid(row = 0, column= 1)
StartButton.grid(row = 1, column= 1)
targetLabel.grid(row = 2, column= 1)
TextBox.grid(row = 3, column=1)

TextBox.insert(tk.END, "notepad.exe")

root.mainloop()
