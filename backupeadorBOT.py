import glob
import os
import asyncio
import telegram
from localConfig import *


class BackupeadorBOT():

	def __init__():
		self.bot = telegram.Bot(mytoken)

	async def sendInfo(self, fileName):
		message = ""
		add2msg = False

		with open(fileName, "r") as file:
		    for line in file:
		        if "Cartridge Information:" in line:
		            add2msg = True
		        elif "Disconnected" in line:
		            add2msg = False
		        if add2msg:
		            message+=str(line)

		if "invalid" in message:
		    message = "Error: unable to read SRAM from cartridge. Make sure that it is well connected and the contacts are clean :)"

		async with self.bot:
		 	await self.bot.send_message(text=message, chat_id=mychatID)


	async def uploadFile(self):
		files = glob.glob(savesdir+'*')
		latest_file = max(files, key=os.path.getctime)

		async with self.bot:
		   	await self.bot.send_document(chat_id=mychatID, document=open(latest_file, 'rb'))

