import RPi.GPIO as GPIO
import time

sensor = 8 
led = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led,False)

print("Initialzing PIR Sensor......")
time.sleep(1)
print("PIR Ready...")
print(" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(led,True)
          print("Motion Detected")
          while GPIO.input(sensor):
              time.sleep(0.1)
      else:
          GPIO.output(led,False)


except KeyboardInterrupt:
    GPIO.cleanup()
