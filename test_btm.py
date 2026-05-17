from gpiozero import Button
from RPLCD.i2c import CharLCD
from signal import pause
import os
import signal
import sys

try:
    lcd = CharLCD('PCF8574', 0x27)
except Exception:
    lcd = CharLCD('PCF8574', 0x3f)

button1 = Button(16, pull_up=True)
button2 = Button(23, pull_up=True)

press_count = 0

def button_pressed():
    global press_count
    press_count += 1
    print(f"Button Pressed! Count: {press_count}")
    
    lcd.clear()
    lcd.write_string("Status: ACTIVE")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Press Count: {press_count}")

def button_released():
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Status: READY ")

def button_shutdown():
    print("\nShutdown button pressed. ")
    lcd.clear()
    lcd.write_string("System Shutdown")
    os.kill(os.getpid(), signal.SIGINT)

button1.when_pressed = button_pressed
button1.when_released = button_released
button2.when_pressed = button_shutdown
    
lcd.clear()
lcd.write_string("Status: READY")
lcd.cursor_pos = (1, 0)
lcd.write_string("Press Count: 0")

try:
    pause()
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("System Shutdown")
    sys.exit(0)