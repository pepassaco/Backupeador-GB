# Backupeador-GB
Machine for automatically backing up your GB/GBC/GBA saves send them to a telegram bot. Built arount the GBxCart v1.4a hardware and the beautiful [FlashGB](https://github.com/lesserkuma/FlashGBX) software.

TODO: Include images

## Installation

As usual: 

```
git clone https://github.com/pepassaco/Backupeador-GB.git --recurse-submodules
python3 -m venv venv
source venv/bin/activate
./install.sh
```
Finally, edit `localConfig.py` according to your needs (with the corresponding token and chat ID of your Telegram bot).


## Usage

As of now (TODO: include GPIO interface with some buttons), just execute the following scipt for backing up DMG/GBC games:

```
./backupGB.sh
```

And this one for GBA games:

```
backupGBA.sh
```

