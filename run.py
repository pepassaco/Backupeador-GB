import RPi.GPIO as GPIO
import time
from backupeador import backupeador


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
			if not GPIO.input(23):
				detectedGB()
			elif not GPIO.input(17):
				detectedGBA()
			else:
				time.sleep(0.01)                    
		except KeyboardInterrupt:
			GPIO.cleanup()       # clean up GPIO on CTRL+C exit
			exit()
	GPIO.cleanup()           # clean up GPIO on normal exit




if __name__ == '__main__':

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	main()