import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31, gpio.OUT)    # IN1
    gpio.setup(33, gpio.OUT)    # IN2
    gpio.setup(35, gpio.OUT)    # IN3
    gpio.setup(37, gpio.OUT)    # IN4

def gameover():
    # set all pins low
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    gpio.output(37, False)
    
def forward(tf):
    init()
    # Left wheels
    gpio.output(31, True) # Left wheels forward direction
    gpio.output(33, False) # Left wheels reverse direction
    # Right wheels
    gpio.output(35, False) # Right wheels reverse direction
    gpio.output(37, True) # Right wheels forward direction
    # Wait
    time.sleep(tf)
    # Send all pins low & cleanup
    gameover()
    gpio.cleanup()

def reverse(tf):
    init()
    # Left wheels
    gpio.output(31, False) # Left wheels forward direction
    gpio.output(33, True) # Left wheels reverse direction
    # Right wheels
    gpio.output(35, True) # Right wheels reverse direction
    gpio.output(37, False) # Right wheels forward direction
    # Wait
    time.sleep(tf)
    # Send all pins low & cleanup
    gameover()
    gpio.cleanup()

def pivotright(tf):
    init()
    # Left wheels
    gpio.output(31, True) # Left wheels forward direction
    gpio.output(33, False) # Left wheels reverse direction
    # Right wheels
    gpio.output(35, True) # Right wheels reverse direction
    gpio.output(37, False) # Right wheels forward direction
    # Wait
    time.sleep(tf)
    # Send all pins low & cleanup
    gameover()
    gpio.cleanup()

def pivotleft(tf):
    init()
    # Left wheels
    gpio.output(31, False) # Left wheels forward direction
    gpio.output(33, True) # Left wheels reverse direction
    # Right wheels
    gpio.output(35, False) # Right wheels reverse direction
    gpio.output(37, True) # Right wheels forward direction
    # Wait
    time.sleep(tf)
    # Send all pins low & cleanup
    gameover()
    gpio.cleanup()

def key_input(event):
    init()
    print("Key:", event)
    key_press = event
    tf = 1

    if key_press.lower() == 'w':
        forward(tf)
    elif key_press.lower() == 's':
        reverse(tf)
    if key_press.lower() == 'a':
        pivotleft(tf)
    if key_press.lower() == 'd':
        pivotright(tf)

while True:
    key_press = input("Select driving mode: ")
    if key_press == 'p':
        break
    key_input(key_press)

