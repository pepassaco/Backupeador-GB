#EDIT THIS!!!
mytoken = "TOKEN"
mychatID='CHAT_ID'
lang = "GAL"




# Strings
if lang == "GAL":
	strErrorCart = "Erro: non foi posible ler a SRAM do cartucho. Asegura que estea ben conectado e que os contactos estean limpos :)"
	strErrorHW = "Erro no hardware. Por favor, avise ao administrador"
	strThx = "Grazas por utilizar o backeador de partidas! \U0001f47e \U0001f579\uFE0F"

elif lang == "ESP":
	strErrorCart = "Error: no fue posible leer la SRAM del cartucho. Asegura que esté bien conectado y que los contactos estén limpios :)"
	strErrorHW = "Error en el hardware. Por favor, avise al administrador"
	strThx = "Gracias por utilizar el backeador de partidas! \U0001f47e \U0001f579\uFE0F"

else:
	strErrorCart = "Error: unable to read SRAM from cartridge. Make sure that it is well connected and the contacts are clean :)"
	strErrorHW = "Hardware error. Please, contact the admin"
	strThx = "Thanks for using the savegame preservation system! \U0001f47e \U0001f579\uFE0F"






# Don't edit unless you know what you are doing
cmdInfo = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'info']
cmdSav = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'backup-save', '--overwrite', '--save-filename-add-datetime', 'Saves/']
savesdir = "Saves/"