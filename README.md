# Backupeador-GB
Machine for automatically backing up your GB/GBC/GBA saves send them to a telegram bot. Built arount the GBxCart v1.4a hardware and the beautiful [FlashGBX](https://github.com/lesserkuma/FlashGBX) software.

TODO: Include images

## Requirements

Just some basic dependencies:

```
sudo apt update
sudo apt upgrade -y
sudo apt install libopenjp2-7
sudo apt install python3-pip
```

## Installation

As usual: 

```
git clone https://github.com/pepassaco/Backupeador-GB.git --recurse-submodules
cd Backupeador-GB
python3 -m venv venv
source venv/bin/activate
./install.sh
```
Finally, edit `localConfig.py` according to your needs (with the corresponding token and chat ID of your Telegram bot).


## Usage

As of now (TODO: include GPIO interface with some buttons for choosing between DMG/GBC and GBA), just execute the following scipt for backing up your games:

```
python3 run.py
```


## Toubleshooting

If your GBxCart is not being recognised by your computer, try the following:

```
sudo systemctl stop brltty-udev.service
sudo systemctl mask brltty-udev.service
sudo systemctl stop brltty.service
sudo systemctl disable brltty.service
```
