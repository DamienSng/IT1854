
mport RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
LED_CLK = 21
LED_DATA = 20

GPIO.setup(LED_CLK, GPIO.OUT)
GPIO.setup(LED_DATA, GPIO.OUT)
GPIO.output(LED_CLK, GPIO.HIGH)
GPIO.output(LED_DATA, GPIO.HIGH)
_state = 10 * [0]
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


def setBits(bits):
    global _state
    for i in range(10):
        if (bits % 2 == 1):
            _state[i] = 0xff
        else:
            _state[i] = 0x00
        bits /= 2                          ##number of '/' limits the number of bars that can light up
    setData()

def setData():

    global _state
    sendData(0)

    for i in range(10):
        sendData(_state[10 - i - 1])

    sendData(0)
    sendData(0)
    GPIO.output(LED_DATA, GPIO.LOW)
    time.sleep(0.01) #sleep 10 microsecs
    for i in range(4):
        GPIO.output(LED_DATA, GPIO.HIGH)
        GPIO.output(LED_DATA, GPIO.LOW)
        
def sendData(data):
    state=GPIO.LOW
    state1=GPIO.LOW
    
    for i in range(16):
        if (data & 0x8000):
            state1 = GPIO.HIGH
        GPIO.output(LED_DATA, state1)
        state = 1 - state
        GPIO.output(LED_CLK, state)
        data = data << 1
        #print(data)        
        
while True:
 
    GPIO.output(TRIG,True)
    time.sleep(1)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print ("distance: ", distance, "cm")
        
        
    if distance < 20:
                      setBits(0b0000000000000011)
                      print ("1 - 20cm")
    elif distance > 20 and distance <= 40:
                      setBits(0b0000000000001100)
                      print ("21 - 40cm")
    elif distance > 40 and distance <= 60:
                      setBits(0b0000000000110000)
                      print ("41 - 60cm")
    elif distance > 60 and distance <= 80:
                      setBits(0b0000000011000000)
                      print ("61 - 80cm")
    elif distance > 80 and distance <= 100:
                      setBits(0b0000001100000000)
                      print ("81 - 100cm")
    else:
                      setBits(0b0000001100000000)
                      time.sleep(1)
                      setBits(0b0000000000000000)                    
                      print (" Above 100")
