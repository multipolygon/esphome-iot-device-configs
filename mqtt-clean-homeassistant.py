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
    return p.parse_args()

args = args()

with open(args.secrets or 'secrets.yaml') as f:
    secrets = yaml.load(f, Loader=yaml.FullLoader)

topic = '/'.join((i for i in [
    secrets['MQTT_PREFIX'],
    'homeassistant',
    '+',
    '+',
    '+',
    'config'
] if i))

client = mqtt.Client("mqtt-clean-homeassistant")

print('Username:', secrets['MQTT_USERNAME'])
client.username_pw_set(secrets['MQTT_USERNAME'], password = secrets['MQTT_PASSWORD'])

messages = []

def on_message(client, userdata, message):
    try:
        if message.retain:
            messages.append([message.topic, message.payload.decode("utf-8")])
    except Exception as e:
        print(e)

client.on_message = on_message

print('Connecting to:', secrets['MQTT_BROKER'])
client.connect(secrets['MQTT_BROKER'])

print('Listening to:', topic)
client.subscribe(topic)

print('...')
client.loop_start()
sleep(3)
client.loop_stop(force=False)
client.disconnect()

last_device = None
skip_device = False

if len(messages) == 0:
    print('No messages received!')

else:
    client.connect(secrets['MQTT_BROKER'])

    print('%d entities found.' % len(messages))
    print('Answer "d" to delete (clean) the following device entities.')
    print('Answer "i" for more device info.')
    print('Answer "s" to skip over the device.')
    print('Press [Enter] to skip with no action.')

    for topic, payload in sorted(messages, key = lambda i: i[0].split('/')[3] + i[0].split('/')[4]):
        cls = topic.split('/')[2]
        dev = topic.split('/')[3]
        ent = topic.split('/')[4]

        if skip_device and last_device == dev:
            pass

        else:
            skip_device = False

            if last_device != dev:
                print('\n%s' % dev)
                last_device = dev

            while True:
                answer = input('  %s: %s ? ' % (cls, ent)).strip()
                if answer == '':
                    break

                elif answer == 's':
                    skip_device = True
                    break

                elif answer == 'd':
                    client.publish(topic, payload=None, retain=True)
                    print('    -> DELETED ')
                    break

                elif answer == 'i':
                    try:
                        print(
                            json.dumps(
                                json.loads(
                                    payload
                                ),
                                sort_keys=False,
                                indent=4
                            )
                        )
                    except:
                        print('[TEXT]', payload)


