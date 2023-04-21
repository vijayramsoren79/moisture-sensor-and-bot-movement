import RPi.GPIO as GPIO
import time

left_sensor = 17
center_sensor = 27
right_sensor = 22

left_motor1 = 18
left_motor2 = 23
right_motor1 = 24
right_motor2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(center_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)
GPIO.setup(left_motor1, GPIO.OUT)
GPIO.setup(left_motor2, GPIO.OUT)
GPIO.setup(right_motor1, GPIO.OUT)
GPIO.setup(right_motor2, GPIO.OUT)

def read_sensors():
    left_value = GPIO.input(left_sensor)
    center_value = GPIO.input(center_sensor)
    right_value = GPIO.input(right_sensor)
    return left_value, center_value, right_value

def move_forward():
    GPIO.output(left_motor1, GPIO.HIGH)
    GPIO.output(left_motor2, GPIO.LOW)
    GPIO.output(right_motor1, GPIO.HIGH)
    GPIO.output(right_motor2, GPIO.LOW)

def move_left():
    GPIO.output(left_motor1, GPIO.LOW)
    GPIO.output(left_motor2, GPIO.HIGH)
    GPIO.output(right_motor1, GPIO.HIGH)
    GPIO.output(right_motor2, GPIO.LOW)

def move_right():
    GPIO.output(left_motor1, GPIO.HIGH)
    GPIO.output(left_motor2, GPIO.LOW)
    GPIO.output(right_motor1, GPIO.LOW)
    GPIO.output(right_motor2, GPIO.HIGH)

try:
    while True:
        left, center, right = read_sensors()
        if center == 1 and left == 0 and right == 0:
            move_forward()
        elif center == 0 and left == 1 and right == 0:
            move_left()
        elif center == 0 and left == 0 and right == 1:
            move_right()
        else:
            GPIO.output(left_motor1, GPIO.LOW)
            GPIO.output(left_motor2, GPIO.LOW)
            GPIO.output(right_motor1, GPIO.LOW)
            GPIO.output(right_motor2, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()