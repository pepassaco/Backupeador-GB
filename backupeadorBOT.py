import telegram
from localConfig import *

class backupeadorBOT():
	def __init__(self):
		self.bot = telegram.Bot(mytoken)

	async def sendInfo(self, message):
		async with self.bot:
			await self.bot.send_message(text=message, chat_id=mychatID, parse_mode='Markdown')

	async def uploadFile(self, latest_file):
		async with self.bot:
			await self.bot.send_document(chat_id=mychatID, document=open(latest_file, 'rb'))