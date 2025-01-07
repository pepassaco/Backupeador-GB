import RPi.GPIO as GPIO
import time
from backupeador import backupeador
from localConfig import pinGB, pinGBA

def detectedGBA():
        print("GBA game selected")
        bckp = backupeador()
        bckp.backupGBA()

def detectedGB():
        print("GBC game selected")
        bckp = backupeador()
        bckp.backupGB()

def main():

        while(True):
                try:
                        if GPIO.input(pinGB):
                                detectedGB()
                        elif GPIO.input(pinGBA):
                                detectedGBA()
                        else:
                                time.sleep(0.05)
                except KeyboardInterrupt:
                        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
                        exit()
        GPIO.cleanup()           # clean up GPIO on normal exit




if __name__ == '__main__':

        print("Starting Backupeador. Project by github.com/pepassaco")
        print("Have fun! :)")

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinGB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pinGBA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        main()
