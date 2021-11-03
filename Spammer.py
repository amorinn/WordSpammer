import pyautogui
import keyboard
import appJar
from time import sleep

def buttonPress(button):
    if(button == "Spam"):
        message = str(app.getEntry("message"))
        sleep(5)
        while True:
            pyautogui.write(message)
            sleep(0.01)
            pyautogui.press("enter")

            if keyboard.is_pressed("esc"):
                break

app = appJar.gui("autoclicker")
app.setSize("300x200")
app.setSticky("new")
app.addLabel("Enter message", row=0)
app.addEntry("message", row=1)
app.addButton("Spam", buttonPress, row=3)
app.setSticky("e")
app.go()





