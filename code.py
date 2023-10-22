import board
import time
import random
import neopixel
import busio
import adafruit_lis3dh
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
from colorpallette import colors



numpix = 8
pixpin = board.A3

ORDER = neopixel.GRB

col =[
    colors.CYBER,
    colors.MINT,
    colors.BLUEY,
    colors.GREEN,
    colors.BLUE,
    colors.CYAN,
    colors.NEON,
    colors.YELLOW,
    colors.RORANGE,

]
x = 1
pixels = neopixel.NeoPixel(pixpin, numpix, brightness=x, auto_write=False,pixel_order = ORDER)

i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D6)
accel = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
accel.range = adafruit_lis3dh.RANGE_4_G
accel.set_tap(1, 100)
THRESHOLD = 150

def trail(color_choice):
    for i in range(numpix):
        pixels[i] = col[color_choice]
        pixels.show()
        time.sleep(0.07)

def filler():
    pixels.fill(col[6])
    pixels.show()
    time.sleep(0.04)

def twinkle():
    for i in range(numpix * 2):
        r = random.randint(0,(numpix-1))
        pixels[r] = col[r]
        pixels.show()
        time.sleep(0.02)
        pixels.fill(0)
        pixels.show()
        time.sleep(0.02)

def turn_off():
    for i in range(numpix):
        pixels[i] = 0
        pixels.show()
        time.sleep(0.04)
c = 1
WAV_FILE_NAME = "twinkle.wav"
while True:

    with AudioOut(board.A0) as audio:  # Speaker connector
    wave_file = open(WAV_FILE_NAME, "rb")
    wave = audiocore.WaveFile(wave_file)

    r = random.randint(0,7)

    x, y, z = accel.acceleration
    accel_total = x * x + z * z
    print(x, y, z)
    time.sleep(0.1)
    if accel_total > THRESHOLD:
        twinkle()
        audio.play(wave)
        print("Twinkle!")
    if accel.tapped:
        c = r
        trail(c)

    trail(c)
    time.sleep(0.5)



# Write your code here :-)
