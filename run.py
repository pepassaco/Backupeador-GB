from backupeador import backupeador
import RPi.GPIO as GPIO 


'''
def detectedGB(channel):  
    print("falling edge detected on 17") 
  
def detectedGBA(channel):  
    print("falling edge detected on 23") 

'''


def main():

	bckp = backupeador()
	
	GPIO.add_event_detect(17, GPIO.FALLING, callback=bckp.backupGB(), bouncetime=300)  
	GPIO.add_event_detect(23, GPIO.FALLING, callback=bckp.backupGB(), bouncetime=300)

	while(True):
		except KeyboardInterrupt:  
			GPIO.cleanup()       # clean up GPIO on CTRL+C exit
	GPIO.cleanup()           # clean up GPIO on normal exit 




if __name__ == '__main__':

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    main()