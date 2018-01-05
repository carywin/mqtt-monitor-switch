# mqtt-monitor-switch
Control the power state of a RPi monitor via MQTT

This requires Paho MQTT to be installed, eg. pip install paho-mqtt

Edit the file to add your broker address, password, etc.

It uses the tvservice and some other hackery to make a HDMI attached monitor sleep/wake in response to MQTT commands.

I use this on a dashboard monitor in my kitchen, so that OpenHAB can switch the dashboard on/off in response to movement from the motion sensor, presence detection, time of day, etc.
