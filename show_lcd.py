import time
import Adafruit_CharLCD as LCD


# Raspberry Pi pin configuration:
lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print message
lcd.message('Hello!')

time.sleep(5.0)

lcd.clear()
lcd.show_cursor(True)
lcd.message('My name is\nBEBE')

time.sleep(5.0)

lcd.clear()
lcd.blink(True)
lcd.message('Start...')

time.sleep(5.0)

lcd.show_cursor(False)
lcd.blink(False)

# Move message
for j in range(2):
    # Move right
    lcd.clear()
    message = 'Move BEBE'
    lcd.message(message)
    move_cnt = lcd_columns-len(message)+1
    for i in range(move_cnt):
        time.sleep(0.5)
        lcd.move_right()

    # create message
    lcd.clear()
    message = ''
    for i in range(14):
        message += ''
    message += '\n       Move BEBE'


    # move left
    lcd.message(message)
    for i in range(move_cnt):
        time.sleep(0.5)
        lcd.move_left()

lcd.clear()
lcd.message('End...')
time.sleep(5.0)

lcd.clear()
lcd.message('Goodbye!')

time.sleep(5.0)

lcd.clear()