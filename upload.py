import glob
import os
import asyncio
import telegram
from localConfig import *

files = glob.glob(savesdir+'*')
latest_file = max(files, key=os.path.getctime)
#print(latest_file)

async def main():
    bot = telegram.Bot(mytoken)
    async with bot:
    	#await bot.send_message(text='¡Hola, Mundo!', chat_id='@Backupeador_GB_GBA')
    	await bot.send_document(chat_id=mychatID, document=open(latest_file, 'rb'))


if __name__ == '__main__':
    asyncio.run(main())