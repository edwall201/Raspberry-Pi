from gpiozero import Button
from signal import pause

button = Button(16, pull_up=True)
def button_pressed():
    print("Press!")

def button_released():
    print("Released")

button.when_pressed = button_pressed
button.when_released = button_released

print("--- Btm test begin ---")

pause()
