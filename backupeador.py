import asyncio
import subprocess
import sys
from backupeadorBOT import backupeadorBOT
from localConfig import *


class backupeador():
	def backupGB(self):
		myBOT = backupeadorBOT()
		gameInfo = subprocess.run(cmdInfoGB, capture_output=True, text=True)
		[message, noterror] = self.infoParserGB(gameInfo.stdout)
		asyncio.run(myBOT.sendInfo(message))
		if noterror:
			subprocess.run(cmdSavGB, stdout=subprocess.DEVNULL)
			asyncio.run(myBOT.uploadLatestFile(savesdir))
			if allow_bckp_ROM:
				asyncio.run(myBOT.sendInfo(strDumpingROM))
				subprocess.run(cmdROMGB, stdout=subprocess.DEVNULL)
				asyncio.run(myBOT.uploadLatestFile(ROMsdir))
			asyncio.run(myBOT.sendInfo(strThx))

	def backupGBA(self):
		myBOT = backupeadorBOT()

		gameInfo = subprocess.run(cmdInfoGBA, capture_output=True, text=True)
		subprocess.run(cmdSavGBA, stdout=subprocess.DEVNULL)
		[message, noterror] = self.infoParserGBA(gameInfo.stdout)
		asyncio.run(myBOT.sendInfo(message))
		if noterror:
			asyncio.run(myBOT.uploadLatestFile(savesdir))
			if allow_bckp_ROM:
				asyncio.run(myBOT.sendInfo(strDumpingROM))
				subprocess.run(cmdROMGBA, stdout=subprocess.DEVNULL)
				asyncio.run(myBOT.uploadLatestFile(ROMsdir))
			asyncio.run(myBOT.sendInfo(strThx))

	def infoParserGB(self, textOutput):
		if textOutput is None:
			message = strErrorCart
			noterror = False
			return(message, noterror)
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
	
	def infoParserGBA(self, textOutput):
		if textOutput is None:
			message = strErrorCart
			noterror = False
			return(message, noterror)
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