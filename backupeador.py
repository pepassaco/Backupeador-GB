import asyncio
import subprocess
import os
import glob
from backupeadorBOT import backupeadorBOT
from localConfig import *


class backupeador():
	def backupGB(self):
		myBOT = backupeadorBOT()
		asyncio.run(myBOT.sendInfo(strInto))
		gameInfo = subprocess.run(cmdInfoGB, capture_output=True, text=True)
		[message, is_error, has_save] = self.infoParser(gameInfo.stdout)
		asyncio.run(myBOT.sendInfo(message))
		if not is_error:
			if not has_save:
				asyncio.run(myBOT.sendInfo(strErrorNoSave))
			else:
				subprocess.run(cmdSavGB, stdout=subprocess.DEVNULL)
				save_file = self.get_latest_dumped_file(savesdir)
				if save_file is None:
					asyncio.run(myBOT.sendInfo(strErrorCart))
				else:
					asyncio.run(myBOT.uploadFile(save_file))
					if not keep_dumped_saves:
						os.remove(save_file)
					if allow_bckp_ROM:
						asyncio.run(myBOT.sendInfo(strDumpingROM))
						subprocess.run(cmdROMGB, stdout=subprocess.DEVNULL)
						ROM_file = self.get_latest_dumped_file(ROMsdir)
						if ROM_file is None:
							asyncio.run(myBOT.sendInfo(strErrorCart))
						else:
							asyncio.run(myBOT.uploadFile(ROM_file))
							if not keep_dumped_ROMs:
								os.remove(ROM_file)

					asyncio.run(myBOT.sendInfo(strThx))

	def backupGBA(self):
		myBOT = backupeadorBOT()
		asyncio.run(myBOT.sendInfo(strInto))
		gameInfo = subprocess.run(cmdInfoGBA, capture_output=True, text=True)
		[message, is_error, has_save] = self.infoParser(gameInfo.stdout)
		asyncio.run(myBOT.sendInfo(message))
		if not is_error:
			if not has_save:
				asyncio.run(myBOT.sendInfo(strErrorNoSave))
			else:
				subprocess.run(cmdSavGBA, stdout=subprocess.DEVNULL)
				save_file = self.get_latest_dumped_file(savesdir)
				if save_file is None:
					asyncio.run(myBOT.sendInfo(strErrorCart))
				else:
					asyncio.run(myBOT.uploadFile(save_file))
					if not keep_dumped_saves:
						os.remove(save_file)
					if allow_bckp_ROM:
						asyncio.run(myBOT.sendInfo(strDumpingROM))
						subprocess.run(cmdROMGBA, stdout=subprocess.DEVNULL)
						ROM_file = self.get_latest_dumped_file(ROMsdir)
						if ROM_file is None:
							asyncio.run(myBOT.sendInfo(strErrorCart))
						else:
							asyncio.run(myBOT.uploadFile(ROM_file))
							if not keep_dumped_ROMs:
								os.remove(ROM_file)
					asyncio.run(myBOT.sendInfo(strThx))

	def infoParser(self, textOutput):
		if textOutput is None or "Invalid" in textOutput:
			message = strErrorCart
			is_error = True
			return(message, is_error, False)
		if len(textOutput) < 2:
			message = strErrorHW
			is_error = True
			return(message, is_error, False)
		is_error = False
		message = ""
		add2msg = False
		has_save = False
		lines = textOutput.split("\n")
		for line in lines:
			if "Cartridge Information:" in line:
				add2msg = True
			elif "Disconnected" in line:
				add2msg = False
			if add2msg:
				if line.startswith("Save Type:"):
					has_save = "None" not in line
				message+=str(line)+'\n'
		return(message, is_error, has_save)

	def get_latest_dumped_file(self, dir):
		files = glob.glob(dir+'*')
		if len(files) == 0:
			return None
		latest_file = max(files, key=os.path.getctime)
		if latest_file.endswith('.md'):
			return None
		return(latest_file)