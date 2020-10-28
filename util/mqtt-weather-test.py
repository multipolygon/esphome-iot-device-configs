import paho.mqtt.client as mqtt
import yaml
from argparse import ArgumentParser
from time import sleep
from random import randint

def args():
    p = ArgumentParser()
    p.add_argument("--secrets", '-s', action="store", type=str, help='Transfer specified file as secrets.json')
    p.add_argument("--topic", '-t', action="store", type=str, help='Topic to publish to.')
    return p.parse_args()

args = args()

with open(args.secrets or 'secrets.yaml') as f:
    secrets = yaml.load(f, Loader=yaml.FullLoader)

client = mqtt.Client("mqtt-clean-homeassistant")

client.username_pw_set(secrets['MQTT_USERNAME'], password = secrets['MQTT_PASSWORD'])

client.connect(secrets['MQTT_BROKER'])

types = [
    "cloudy",
    "cloudy-alert",
    "cloudy-arrow-right",
    "fog",
    "hail",
    "hazy",
    "hurricane",
    "lightning",
    "lightning-rainy",
    "night",
    "night-partly-cloudy",
    "partly-cloudy",
    "partly-lightning",
    "partly-rainy",
    "partly-snowy",
    "partly-snowy-rainy",
    "pouring",
    "rainy",
    "snowy",
    "snowy-heavy",
    "snowy-rainy",
    "sunny",
    "sunny-alert",
    "sunny-off",
    "sunset",
    "sunset-down",
    "sunset-up",
    "tornado",
    "windy",
    "windy-variant",
]

while True:
    for t in types:
        print(t)
        client.publish('weather/forecast/today/condition', payload=t, retain=True)
        client.publish('weather/forecast/today/high', payload=randint(-10, 50), retain=True)
        client.publish('weather/forecast/today/wind/gust', payload=randint(0, 100), retain=True)
        sleep(1)
