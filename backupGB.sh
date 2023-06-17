python FlashGBX/run.py --cli --cfgdir subdir --mode dmg --action info > info.txt
python sendCartData.py
rm -rf info.txt
python FlashGBX/run.py --cli --cfgdir subdir --mode dmg --action backup-save --overwrite --save-filename-add-datetime Saves/
python upload.py