"""Your code creates a desktop window with a button labeled "Take Screenshot". When you click that button, 
Python takes a photo of your screen and opens a "Save As" file box so you can pick a folder to save your picture named screenshot.png."""

import tkinter as tk #making the windowed apps with buttons
from tkinter.filedialog import * #filedialog, which is the special sub-tool inside Tkinter that opens the "Save As" pop-up window on your computer.
import pyautogui #control the screen and mouse and keyboard, extenal module not python built in so you need to install it with pip install pyautogui  
#pip install pyautogui in cmd       

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400) #You create a blank drawing board called a Canvas inside root that is 400 pixels wide and 400 pixels tall.
canvas.pack()  #You tell Tkinter to "pack" (place) the canvas tightly inside the main window.

def take_screenshot():
    my_screenshot = pyautogui.screenshot() #pyautogui.screenshot() to take a snapshot of your full screen and saves the image object into the variable my_screenshot
    save_path = asksaveasfilename()  #Opens a pop-up window asking where you want to save the file and assigns the chosen file path string to save_path
    my_screenshot.save(save_path + "screenshot.png")

button_pattern = tk.Button(text="Take Screenshot", command=take_screenshot, font = 10)
canvas.create_window(200, 200, window=button_pattern)
root.mainloop()




