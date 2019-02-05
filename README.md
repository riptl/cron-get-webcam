# ⏰ Cron webcam archiver

 * Archive [single picture webcams](https://www.augsburg.de/fileadmin/user_upload/header/webcam/webcamdachspitz/B_Rathausplatz_Dachspitz_00.jpg)
 * Simple and reliable setup (32 lines of code)
 * Zero config
 * Requirements: `python3` + `requests` + `cron`
 * One picture per invocation
 * Only new pictures get saved
 * Easy folder structure: `yyyy-mm-dd/hhmmss` (UTC)

### Watch (every 5 seconds)
```sh
watch -n5 cron-get-webcam.py folder http://example.org/webcam-url.jpg
```

### Cron (every minute)
```sh
crontab -e
* * * * * cron-get-webcam.py folder http://example.org/webcam-url.jpg
```

> by terorie, 2019
>
> also check out https://github.com/The-Eye-Team and https://the-eye.eu
