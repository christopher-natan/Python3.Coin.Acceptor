# @author        Christopher M. Natan
# @version       1.0


import RPi.GPIO as GPIO
import time


GPIO_COIN_ACCEPTOR_PIN = 15


class CoinAcceptor:
    loop_counter = 0
    counter = 0

    def __init__(self):
        self.set_gpio()

    def set_gpio(self):
        print("Coin acceptor is listening..")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_COIN_ACCEPTOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def set(self):
        while True:
            if GPIO.input(GPIO_COIN_ACCEPTOR_PIN) == 1:
                time.sleep(0.1)
                self.loop_counter = 0
                self.counter = self.counter + 1
            else:
                time.sleep(0.01)
                self.loop_counter = self.loop_counter + 1

    def reset(self):
        self.counter = 0
        self.loop_counter = 0

try:
    CoinAcceptor = CoinAcceptor()
    CoinAcceptor.set()
    GPIO.cleanup()

except PermissionError:
    print("PermissionError...")
except SystemExit:
    print("SystemExit...")
except KeyboardInterrupt:
    print("KeyboardInterrupt...")
    GPIO.cleanup()