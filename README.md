# ⏰ Cron webcam archiver

 * Archive [single picture webcams](https://www.augsburg.de/fileadmin/user_upload/header/webcam/webcamdachspitz/B_Rathausplatz_Dachspitz_00.jpg)
 * Simple and reliable setup (32 lines of code)
 * Zero config
 * Requirements: `python3` + `requests` + `cron`

### Setup

```sh
# Download script
wget https://raw.githubusercontent.com/terorie/cron-get-webcam/master/cron-get-webcam.py
chmod +x cron-get-webcam.py
mv cron-get-webcam.py /usr/bin/

# Create cron job (replace dir and url)
crontab -e
*/30 * * * * cron-get-webcam.py dir url
```
