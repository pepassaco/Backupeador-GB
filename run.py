import RPi.GPIO as GPIO
import time
from backupeador import backupeador


def detectedGBA(channel):
	print("GBA game selected")
	bckp = backupeador()
	bckp.backupGBA()

def detectedGB(channel):
	print("GBC game selected")
	bckp = backupeador()
	bckp.backupGB()



def main():

	GPIO.add_event_detect(17, GPIO.FALLING, callback=detectedGBA, bouncetime=300)
	GPIO.add_event_detect(23, GPIO.FALLING, callback=detectedGB, bouncetime=300)

	while(True):
		try:
			time.sleep(1)                    
		except KeyboardInterrupt:
			GPIO.cleanup()       # clean up GPIO on CTRL+C exit
			exit()
	GPIO.cleanup()           # clean up GPIO on normal exit




if __name__ == '__main__':

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	main()