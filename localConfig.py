#EDIT THESE!!!

mytoken = "YOUR_TOKEN"
mychatID="YOUR_CHANNEL_CHAT_ID"
lang = "GAL"

pinGBA = 23
pinGB = 25

allow_bckp_ROM = True
keep_dumped_saves = False
keep_dumped_ROMs = True

savesdir = "Saves/"
ROMsdir = "ROMs/"

owner_name = "Museo do Videoxogo"






# Strings
if lang == "GAL":
        strInto = "Benvido ao *Backupeador* de Game Boy e Game Boy Advance do *" + owner_name + "*!"
        strErrorCart = "Erro: non foi posible ler a SRAM do cartucho. Asegura que estea ben conectado, pulsar o botón correcto (GB/GBA) e que os contactos estean limpos :)"
        strErrorHW = "Erro no hardware. Por favor, avise ao administrador"
        strErrorNoSave = "Non é posible facer unha copia de seguridade da partida gardada porque este xogo non ten capacidade de gardado! \U0001F605 (O cartucho non ten memoria SRAM)"
        strDumpingROM = "Facendo unha copia da ROM. Isto pode levar ata 5min nalgúns xogos de GBA \u231B \n\n \u26A0\uFE0F Por favor, non toque o cartucho ata que remate o proceso! \u26A0\uFE0F"
        strThx = "Lembra que tes 24h para descargar os teus arquivos \u23F2\uFE0F \n\nPasado este prazo, éstes serán borrados automáticamente\u274C \n\nGrazas por utilizar o backupeador de partidas! \U0001f47e \U0001f579\uFE0F"

elif lang == "ESP":
        strInto = "Bienvenido al *Backupeador* de Game Boy y Game Boy Advance del *" + owner_name + "*!"
        strErrorCart = "Error: no fue posible leer la SRAM del cartucho. Asegura que esté bien conectado, pulsar el botón correcto (GB/GBA) y que los contactos estén limpios :)"
        strErrorHW = "Error en el hardware. Por favor, avise al administrador"
        strErrorNoSave = "No es posible hacer una copia de seguridad de la partida guardada porque este juego no tiene capacidad de guardado! \U0001F605 (El cartucho no tiene memoria SRAM)"
        strDumpingROM = "Haciendo una copia de la ROM, esto puede tardar hasta 5min en algunos juegos de GBA \u231B \n\n \u26A0\uFE0F Por favor, no toque el cartucho hasta que remate el proceso! \u26A0\uFE0F"
        strThx = "Recuerda que tienes 24h para descargar tus archivos \u23F2\uFE0F Pasado este plazo, éstos se borrarán automáticamente\u274C \n\nGracias por utilizar el backupeador de partidas! \U0001f47e \U0001f579\uFE0F"
else:
        strInto = "Welcome to the *Backupeador* for Game Boy and Game Boy Advance from the *" + owner_name + "*!"
        strErrorCart = "Error: unable to read SRAM from cartridge. Make sure that it is well connected, that you pressed the right button (GB/GBA) and that the contacts are clean :)"
        strErrorHW = "Hardware error. Please, contact the admin"
        strErrorNoSave = "It was not possible to make a backup of the save because this game is not capable of storing saves! \U0001F605 (The cartridge has no SRAM memory)"
        strDumpingROM = "Backing up ROM, this can take up to 5min for some GBA games \u231B \n\n \u26A0\uFE0F Please, do not touch the cartridge until the process finishes or data can be corrupted! \u26A0\uFE0F"
        strThx = "Remember that you have 24h to download your files \u23F2\uFE0F After this time, they will be deleted automatically\u274C \n\nThanks for using the savegame preservation system! \U0001f47e \U0001f579\uFE0F"



# Don't edit unless you know what you are doing
cmdInfoGB = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'info']
cmdSavGB = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'backup-save', '--overwrite', '--save-filename-add-datetime', savesdir]
cmdROMGB = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'dmg', '--action', 'backup-rom', '--overwrite', '--save-filename-add-datetime', ROMsdir]
cmdInfoGBA = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'agb', '--action', 'info']
cmdSavGBA = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'agb', '--action', 'backup-save', '--overwrite', '--save-filename-add-datetime', savesdir]
cmdROMGBA = ['python3', 'FlashGBX/run.py', '--cli', '--cfgdir', 'subdir', '--mode', 'agb', '--action', 'backup-rom', '--overwrite', '--save-filename-add-datetime', ROMsdir]