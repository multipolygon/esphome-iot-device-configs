# ESPHome Configs

## Resources

https://esphome.io/guides/getting_started_command_line.html

https://esphome.io/components/wifi.html

https://esphome.io/components/mqtt.html

https://www.home-assistant.io/docs/mqtt/discovery

https://www.home-assistant.io/components/esphome/

## Install

    pipenv install

    pipenv run esphome device_name.yaml run

## Wemos D1 Mini (ESP8266) v2.0.0

    A0 = 0 # Analog input, max 3.3V
    D0 = RESET = WAKE_UP = 16
    D1 = SCL = 5
    D2 = SDA = 4
    D3 = 0 # 10k Pull-up - no low input!
    D4 = LED = 2 # 10k Pull-up - no low input!
    D5 = SCK = 14
    D6 = MISO = 12
    D7 = MOSI = 13 
    D8 = SS = 15 # 10k Pull-down - no high input!
