from gpiozero import Button
from RPLCD.i2c import CharLCD
from signal import pause
import sys

try:
    lcd = CharLCD('PCF8574', 0x27)
except Exception:
    lcd = CharLCD('PCF8574', 0x3f)

button = Button(16, pull_up=True)

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

button.when_pressed = button_pressed
button.when_released = button_released

print("--- Integrated LCD & Button Test Started ---")

lcd.clear()
lcd.write_string("Status: READY")
lcd.cursor_pos = (1, 0)
lcd.write_string("Press Count: 0")

try:
    pause()
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("System Shutdown")
    print("\nProgram closed cleanly by user.")
    sys.exit(0)