import asyncio
import telegram
from localConfig import *


message = ""
add2msg = False

with open("info.txt", "r") as file:
    for line in file:
        if "Cartridge Information:" in line:
            add2msg = True
        elif "Disconnected" in line:
            add2msg = False

        if add2msg:
            message+=str(line)


async def main():
    bot = telegram.Bot(mytoken)
    async with bot:
    	await bot.send_message(text=message, chat_id=mychatID)


if __name__ == '__main__':
    asyncio.run(main())