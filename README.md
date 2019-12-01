# clock-project

Open main.py in a Python environment and hit run. Simple!

Setting time without WiFi:

If you have WiFi, you are in luck! I was using Raspberry Pi 2, so I wasn't. If you are in luck, ignore all of this!

There exists a soft-hwclock file that can be potentially run. This will not set the Pi to the exact "real" time, but it might offer an okay approximation.

Manually, the Pi can be set if you know the real time. Open the command prompt, and use the following command:

sudo date -s "Fri Nov 29 13:45:00 PST 2019"

Remember to change the text so that the day of week, month/day, time, time zone, and year are correct!
