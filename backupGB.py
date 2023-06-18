import asyncio
import subprocess
import sys
from backupeadorBOT import backupeadorBOT


async def main():
	#myBOT = backupeadorBOT()

	subprocess.run()
	gameInfo = subprocess.run(
	    ["python3 FlashGBX/run.py --cli --cfgdir subdir --mode dmg --action info"], capture_output=True, text=True
	)
	print("stdout:", gameInfo.stdout)

	#myBOT.sendInfo(fileName)
	#myBOT.uploadFile()


if __name__ == '__main__':
    asyncio.run(main())



'''
python3 FlashGBX/run.py --cli --cfgdir subdir --mode dmg --action info > info.txt
python3 sendCartData.py
rm -rf info.txt
python3 FlashGBX/run.py --cli --cfgdir subdir --mode dmg --action backup-save --overwrite --save-filename-add-datetime Saves/
python3 upload.py
'''