import Jetson.GPIO as GPIO
import time

# Definisikan pin GPIO yang akan digunakan
DIR_PIN = 20   # Pin untuk arah
STEP_PIN = 21  # Pin untuk langkah
DELAY = 0.001  # Delay antar langkah dalam detik

# Setup pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

# Fungsi untuk menggerakkan motor stepper
def move_stepper(steps, delay):
    # Arahkan motor (0 atau 1)
    GPIO.output(DIR_PIN, GPIO.HIGH)  # Ganti ke GPIO.LOW jika ingin arah berlawanan
    
    for _ in range(steps):
        # Buat pulse untuk langkah
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    # Gerakkan motor 1000 langkah
    move_stepper(1000, DELAY)
finally:
    # Reset pin GPIO
    GPIO.cleanup()
