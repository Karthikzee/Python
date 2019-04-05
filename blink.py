import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time                              # calling for time to provide delays in program

n = int(input("Give the number of blinks: "))
for i in range(0, n):           # Loop to blink desired number of times
    IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
    IO.setup(40,IO.OUT)             # initialize digital pin40 as an output.
    IO.output(40,1)                      # turn the LED on (making the voltage level HIGH)
    time.sleep(0.5)                         # sleep for a second
    IO.cleanup()                         # turn the LED off (making all the output pins LOW)
    time.sleep(0.1)                        #sleep for a second    

