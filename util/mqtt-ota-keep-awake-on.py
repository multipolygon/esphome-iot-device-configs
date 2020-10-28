import os
import datetime
import re
import paho.mqtt.client as mqtt
import json
import yaml
from argparse import ArgumentParser
from time import sleep

def args():
    p = ArgumentParser()
    p.add_argument("--secrets", '-s', action="store", type=str, help='Transfer specified file as secrets.json')
    p.add_argument("--payload", '-p', action="store", type=str, help='ON or OFF')
    return p.parse_args()

args = args()

with open(args.secrets or 'secrets.yaml') as f:
    secrets = yaml.load(f, Loader=yaml.FullLoader)

client = mqtt.Client("mqtt-ota-keep-awake")

print('Username:', secrets['MQTT_USERNAME'])
client.username_pw_set(secrets['MQTT_USERNAME'], password = secrets['MQTT_PASSWORD'])

client.connect(secrets['MQTT_BROKER'])

topic = '/'.join((i for i in [
    secrets['MQTT_PREFIX'],
    'esphome_ota_keep_awake'
] if i))

client.publish(topic, payload=args.payload, retain=True)
