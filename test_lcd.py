from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)

try:
    lcd.clear()
    lcd.write_string('Hello Edward!')
    
    lcd.cursor_pos = (1, 0)
    lcd.write_string('Pi 4B Testing...')
    
    print("Press ctrl+c to end")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    lcd.clear()
    print("\nEnd Testing")
