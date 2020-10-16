import os
import datetime
import re
import paho.mqtt.client as mqtt
import json
import yaml
from argparse import ArgumentParser

def args():
    p = ArgumentParser()
    p.add_argument("--secrets", '-s', action="store", type=str, help='Transfer specified file as secrets.json')
    p.add_argument("--ignore-retained", '-r', action="store_true", help='Ignore retained messages.')
    p.add_argument("--topic", '-t', action="store", type=str, help='MQTT topic to subscribe to.')
    return p.parse_args()

args = args()

with open(args.secrets or 'secrets.yaml') as f:
    secrets = yaml.load(f, Loader=yaml.FullLoader)

topic = args.topic or '/'.join((i for i in [
    secrets['MQTT_PREFIX'],
    '#',
] if i))

client = mqtt.Client("mqtt-listen")

print('Username:', secrets['MQTT_USERNAME'])
client.username_pw_set(secrets['MQTT_USERNAME'], password = secrets['MQTT_PASSWORD'])

def on_message(client, userdata, message):
    try:
        if not (args.ignore_retained and message.retain):
            print("")
            print("[%s] %s:" % (message.retain and "PERMANENT" or str(datetime.datetime.now()), message.topic))
            text = message.payload.decode("utf-8")
            try:
                print(
                    json.dumps(
                        json.loads(
                            text
                        ),
                        sort_keys=False,
                        indent=4
                    )
                )
            except:
                print('[TEXT]', text)

    except Exception as e:
        print(e)

client.on_message = on_message

print('Connecting to:', secrets['MQTT_BROKER'])
client.connect(secrets['MQTT_BROKER'])

print('Listening to:', topic)
client.subscribe(topic)

client.loop_forever()
