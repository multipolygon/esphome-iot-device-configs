import paho.mqtt.client as mqtt
import yaml
from time import sleep

with open('secrets_ag.yaml') as f:
    secrets = yaml.load(f, Loader=yaml.FullLoader)

topic = 'notify/#'

client = mqtt.Client("mqtt-clean-homeassistant")

print('Username:', secrets['MQTT_USERNAME'])
client.username_pw_set(secrets['MQTT_USERNAME'], password = secrets['MQTT_PASSWORD'])

messages = []

def on_message(client, userdata, message):
    try:
        if message.retain:
            messages.append(message.topic)
            print(message.topic, message.payload)
    except Exception as e:
        print(e)

client.on_message = on_message

print('Connecting to:', secrets['MQTT_BROKER'])
client.connect(secrets['MQTT_BROKER'])

print('Listening to:', topic)
client.subscribe(topic)

print('...')
client.loop_start()
sleep(1)
client.loop_stop(force=False)
client.disconnect()

if len(messages) == 0:
    print('No messages received!')

else:
    client.connect(secrets['MQTT_BROKER'])

    print('%d entities found.' % len(messages))
    
    for topic in messages:
        # print('Clean:', topic);
        client.publish(topic, payload=None, retain=True)

        


