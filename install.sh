sudo apt update
sudo apt upgrade -y
sudo apt install libopenjp2-7
sudo apt install python3-pip
pip3 install FlashGBX
pip3 install python-telegram-bot
pip3 install pyserial
pip3 install pillow
sudo systemctl stop brltty-udev.service
sudo systemctl mask brltty-udev.service
sudo systemctl stop brltty.service
sudo systemctl disable brltty.service