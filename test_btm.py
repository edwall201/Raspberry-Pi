from gpiozero import Button
from RPLCD.i2c import CharLCD
from signal import pause
import sys

try:
    lcd = CharLCD('PCF8574', 0x27)
except Exception:
    lcd = CharLCD('PCF8574', 0x3f)

button1 = Button(16, pull_up=True)
button2 = Button(23, pull_up=True)
active = False
is_standby = False
press_count = 0

def button_pressed():
    global press_count, active, is_standby     
    
    if is_standby:
        return
        
    lcd.clear()
    
    if not active:
        active = True
        print("System Activated via First Press")
        lcd.write_string("Status: READY")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Count: 0")
    else:
        press_count += 1
        print(f"Button Pressed! Count: {press_count}")
        lcd.write_string("Status: READY")
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f"Count: {press_count}")

def button_shutdown():
    global is_standby, active, press_count
    
    is_standby = not is_standby
    lcd.clear()
    
    if is_standby:
        lcd.write_string("Standby")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Red to return")
        print("\nEntering Standby Mode...")
        try:
            lcd.no_backlight()
        except AttributeError:
            pass
    else:
        print("Waking up from Standby!")
        
        try:
            lcd.backlight()
        except AttributeError:
            pass
            
        if not active:
            lcd.write_string("ACTIVE")
           
        else:
            lcd.write_string("Status: READY")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Count: {press_count}")

button1.when_pressed = button_pressed
button2.when_pressed = button_shutdown
    
lcd.clear()
lcd.write_string("ACTIVE")
lcd.cursor_pos = (1, 0)
lcd.write_string("Yellow to start")

try:
    pause()
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("System Shutdown")
    sys.exit(0)