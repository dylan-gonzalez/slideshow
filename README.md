```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt install python3-tk
```

Ubuntu server:
```
sudo Xorg :0 vt1 &
export DISPLAY=:0

python3 slideshow.py
```

Put them in systemd services:
`/etc/systemd/system/xorg.service`:
```
[Unit]
Description=Start Xorg Server
After=systemd-user-sessions.service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/Xorg :0 -config /etc/X11/xorg.conf vt1
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/slideshow/.Xauthority
Restart=always

[Install]
WantedBy=graphical.target
```
Make sure `allowed_users=anybody` in `/etc/X11/Xwrapper.config`.

`/etc/systemd/system/slideshow.service`:
```
[Unit]
Description=Run Slideshow Python Script
After=xorg.service
Requires=xorg.service

[Service]
Type=simple
ExecStartPre=/bin/sleep 10
ExecStart=/home/slideshow/slideshow/startup.sh
User=slideshow
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/slideshow/.Xauthority

[Install]
WantedBy=default.target
```

Disable automatic screen blanking
`/etc/systemd/system/disable_screen_blanking.service`:
```
[Unit]
Description=Disable Automatic Screen Blanking
After=xorg.service
Requires=xorg.service

[Service]
Type=simple
ExecStartPre=/bin/sleep 10
ExecStart=/home/slideshow/slideshow/disable_screen_blanking.sh
Environment=DISPLAY=:0

[Install]
WantedBy=default.target
```

`/etc/systemd/sleep.conf`:
```
IdleAction=ignore
```

`/etc/systemd/logind.conf`:
```
IdleAction=ignore
```

# To Do

- [ ] play audio
      - ideally connect to Spotify API, but I think this requires OAuth
      - local mp4 files
- [ ] display image metadata
- [ ] fix fade in/out performance issues on pi
- [ ] automatic scraping for images from NGA
- [ ] access image files from server on network
