#EDIT THIS!!!
mytoken = "YOUR_TOKEN"
mychatID='YOUR_CHANNEL_CHAT_ID'
lang = "GAL"

pinGBA = 23
pinGB = 25

allow_bckp_ROM = True

# Strings
if lang == "GAL":
        strErrorCart = "Erro: non foi posible ler a SRAM do cartucho. Asegura que estea ben conectado e que os contactos estean limpos :)"
        strErrorHW = "Erro no hardware. Por favor, avise ao administrador"
        strDumpingROM = "Facendo unha copia da ROM. Isto pode levar ata de 5min nalgunhos xogos de GBA. Por favor, non toque o cartucho ata que remate o proceso."
        strThx = "Grazas por utilizar o backupeador de partidas! \U0001f47e \U0001f579\uFE0F"

elif lang == "ESP":
        strErrorCart = "Error: no fue posible leer la SRAM del cartucho. Asegura que esté bien conectado y que los contactos estén limpios :)"
        strErrorHW = "Error en el hardware. Por favor, avise al administrador"
        strDumpingROM = "Haciendo una copia de la ROM, esto puede tardar hasta 5min en algunos juegos de GBA. Por favor, no toque el cartucho hasta que remate el proceso."
        strThx = "Gracias por utilizar el backupeador de partidas! \U0001f47e \U0001f579\uFE0F"
else:
        strErrorCart = "Error: unable to read SRAM from cartridge. Make sure that it is well connected and the contacts are clean :)"
        strErrorHW = "Hardware error. Please, contact the admin"
        strDumpingROM = "Backing up ROM, this can take up to 5min for some GBA games. Please, do not touch the cartridge until the process finishes or data can be corrupted."
        strThx = "Thanks for using the savegame preservation system! \U0001f47e \U0001f579\uFE0F"






# Don't edit unless you know what you are doing
cmdInfoGB = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'info']
cmdSavGB = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'backup-save', '--overwrite', '--save-filename-add-datetime', 'Saves/']
cmdROMGB = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'backup-rom', '--overwrite', '--save-filename-add-datetime', 'Saves/']
cmdInfoGBA = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'agb', '--action', 'info']
cmdSavGBA = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'agb', '--action', 'backup-save', '--overwrite', '--save-filename-add-datetime', 'Saves/']
cmdROMGBA = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'agb', '--action', 'backup-rom', '--overwrite', '--save-filename-add-datetime', 'Saves/']
savesdir = "Saves/"
