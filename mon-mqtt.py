#!/usr/bin/python
import paho.mqtt.client as mqtt
import sys
import signal
import os
from subprocess import call
import time

print("Kitchen Monitor Switch")

new_env = os.environ.copy()
new_env['DISPLAY'] = ':0'

def sigint_handler(signal, frame):
        print("Exiting")
        sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def monitor_on():
    print("Switch on")
    call(["/opt/vc/bin/tvservice","-p"])
    call(["xset","dpms","force","on"], env=new_env)
    call(["fbset","-depth","8"])
    call(["fbset","-depth","16"])
    call("xrefresh", env=new_env)
    client.publish("kmon/state", "ON")

def monitor_off():
    print("Switch off")
    call(["/opt/vc/bin/tvservice","-o"])
    client.publish("kmon/state", "OFF")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("kmon/cmd/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == 'kmon/cmd':
      if str(msg.payload) == 'ON':
        monitor_on()
      if str(msg.payload) == 'OFF':
        monitor_off()

# Set up and connect to MQTT broker
client = mqtt.Client(client_id="<Client id")
client.username_pw_set("<username>", password="<password>")
client.on_connect = on_connect
client.on_message = on_message
client.connect("<broker address>", 1883, 60)
print("Running...")
client.publish("kmon/state", "ON")
client.loop_forever()
