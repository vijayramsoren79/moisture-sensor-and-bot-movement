import RPi.GPIO as GPIO
import time

sensor_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

while True:
    moisture_value = GPIO.input(sensor_pin)
    if moisture_value == GPIO.HIGH:
        print("Soil is dry")
    else:
        print("Soil is moist")
    print("Moisture value: ", moisture_value)
    time.sleep(1)
