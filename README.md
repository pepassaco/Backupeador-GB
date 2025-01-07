# Backupeador-GB
Machine for automatically backing up your GB/GBC/GBA saves send them to a telegram bot. Built arount the GBxCart v1.4a hardware and the beautiful [FlashGBX](https://github.com/lesserkuma/FlashGBX) software.

TODO: Include images


## Hardware

The Bill of Materials for this project is as follows:

- GBxCart v1.4 or later
- A Raspberry Pi (3D printed case is adapted for a Zero W but any other board will get the job done file)
- Female USB-C connector with M12 nut ([example](https://es.aliexpress.com/item/1005005353938938.html))
- Male micro-USB connector
- Two round buttons (3D printed case is adapted for [DS-211 buttons](https://es.aliexpress.com/item/1005004732960774.html))

TODO: Include simple schematic


## Installation

0. Disconnect the USB wire going from the GBxCart to the Raspberry Pi

1. Install some basic dependencies:

```
sudo apt update
sudo apt upgrade -y
sudo apt install libopenjp2-7 python3-pip
```

2. Install Backupeador as usual: 

```
git clone https://github.com/pepassaco/Backupeador-GB.git --recurse-submodules
cd Backupeador-GB
./install.sh
```

3. Edit `localConfig.py` according to your needs (with the corresponding **token** and **chat ID** of your Telegram bot).

4. Edit `boot.sh` by replacing `INSTALLATION_PATH` with the **absolute** path to the directory where you cloned the repo.

5. Create a new systemctld service by first executing:

```
sudo nano /lib/systemd/system/backupeador.service
```

Filling the new document with the following code:

```
[Unit]
Description=The backupeador service
After=network-online.target

[Service]
ExecStart=/home/backupeador/Backupeador-GB/boot.sh

[Install]
WantedBy=multi-user.target
```

Saving (CTRL+O) and closing (CTRL+X) the file and enabling the service by doing:

```
sudo chmod 644 /lib/systemd/system/backupeador.service
sudo systemctl daemon-reload
sudo systemctl enable backupeador.service
sudo systemctl start backupeador.service
```

TODO: Remove periodically the siles from the 'Files' folder

6. Connect the GBxCart back to the Raspberry.



## Usage

Press the buttons with a cartridge in the reader and a save file will be automatically generated and sent to a Telegram group!


## Toubleshooting

If your GBxCart is not being recognised by your computer, try the following:

```
sudo systemctl stop brltty-udev.service
sudo systemctl mask brltty-udev.service
sudo systemctl stop brltty.service
sudo systemctl disable brltty.service
```

If it is still not being recognised, unplugging and plugging again the USB cable that connects it to the Raspberry Pi seems to help