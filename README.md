# Backupeador-GB
Machine for automatically backing up your GB/GBC/GBA saves send them to a telegram bot. Built arount the GBxCart v1.4a hardware and the beautiful [FlashGBX](https://github.com/lesserkuma/FlashGBX) software.

TODO: Include images


## Hardware

The Bill of Materials for this project is as follows:

- GBxCart v1.4 or later
- Any Raspberry Pi (I curently unse a model 1B but any should do the job)
- Female USB-C connector with M12 nut ([example](https://es.aliexpress.com/item/1005005353938938.html?spm=a2g0o.productlist.main.23.12103f13FtLXxS&algo_pvid=202b6bab-1dce-4aaa-a6e6-8f7d0727ee7f&algo_exp_id=202b6bab-1dce-4aaa-a6e6-8f7d0727ee7f-11&pdp_npi=3%40dis%21EUR%210.6%210.51%21%21%21%21%21%402100bc5c16871270433503211d07ba%2112000032749371723%21sea%21ES%21171535914&curPageLogUid=2ATkGmBvNDMz))
- Male micro-USB connector
- (optional) Female Ethernet connector with M21 nut ([example](https://es.aliexpress.com/item/1005004863110077.html?spm=a2g0o.productlist.main.23.1fe03a00XDMMWr&algo_pvid=96532dc2-2c98-4aab-bd91-8b40c7b6020d&algo_exp_id=96532dc2-2c98-4aab-bd91-8b40c7b6020d-11&pdp_npi=3%40dis%21EUR%214.71%213.53%21%21%21%21%21%402100b0d116871273445681941d0742%2112000030793371200%21sea%21ES%21171535914&curPageLogUid=2sRKscPJbolo))


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
