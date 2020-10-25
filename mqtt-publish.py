import paho.mqtt.client as mqtt
import yaml
from argparse import ArgumentParser

def args():
    p = ArgumentParser()
    p.add_argument("--secrets", '-s', action="store", type=str, help='Transfer specified file as secrets.json')
    p.add_argument("--topic", '-t', action="store", type=str, help='Topic to publish to.')
    p.add_argument("--message", '-m', action="store", type=str, help='Message.')
    p.add_argument("--retain", '-r', action="store_true", help='Set retained flag on published message.')
    return p.parse_args()

args = args()

with open(args.secrets or 'secrets.yaml') as f:
    secrets = yaml.load(f, Loader=yaml.FullLoader)

client = mqtt.Client("mqtt-clean-homeassistant")

client.username_pw_set(secrets['MQTT_USERNAME'], password = secrets['MQTT_PASSWORD'])

client.connect(secrets['MQTT_BROKER'])

client.publish(args.topic, payload=args.message if args.message != '' else None, retain=args.retain)
