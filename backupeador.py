import asyncio
import subprocess
import sys
from backupeadorBOT import backupeadorBOT
from localConfig import *


class backupeador():
	def backupGB(self):
		myBOT = backupeadorBOT()

		gameInfo = subprocess.run(cmdInfo, capture_output=True, text=True)
		subprocess.run(cmdSav, stdout=subprocess.DEVNULL)

		[message, noterror] = self.infoParserGB(gameInfo.stdout)
		asyncio.run(myBOT.sendInfo(message))
		if noterror:
			asyncio.run(myBOT.uploadLatestFile())
			asyncio.run(myBOT.sendInfo(strThx))


	def infoParserGB(self, textOutput):
		noterror = True
		message = ""
		add2msg = False
		lines = textOutput.split("\n")
		for line in lines:
			if "Cartridge Information:" in line:
				add2msg = True
			elif "Disconnected" in line:
				add2msg = False
			if add2msg:
				message+=str(line)+'\n'

		if "Invalid" in message:
		    message = strErrorCart
		    noterror = False
		elif len(message) == 0:
			message = strErrorHW
			noterror = False

		return(message, noterror)