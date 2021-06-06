# My ESP Home Automation Devices

<table>
<tr>
</tr>
<tr>
<td><a href="./backyard_garden_hub.yaml"><img src="./img/backyard_garden_hub.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./backyard_garden_hub.yaml"><img src="./img/backyard_garden_hub~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./backyard_garden_hub.yaml"><img src="./img/backyard_garden_hub~3~L64.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./camera_diymore.yaml"><img src="./img/camera_diymore.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./camera_m5_xf.yaml"><img src="./img/camera_m5_xf.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./camera_m5_xf.yaml"><img src="./img/camera_m5_xf~3.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./dam_water_level_alarm.yaml"><img src="./img/dam_water_level_alarm.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./dam_water_level_alarm.yaml"><img src="./img/dam_water_level_alarm~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./dam_water_level_alarm.yaml"><img src="./img/dam_water_level_alarm~3.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./garden_trellis.yaml"><img src="./img/garden_trellis.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./garden_trellis.yaml"><img src="./img/garden_trellis~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./garden_trellis.yaml"><img src="./img/garden_trellis~2.png" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./garden_trellis.yaml"><img src="./img/garden_trellis~3.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./living_room_env_sensor.yaml"><img src="./img/living_room_env_sensor.png" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./living_room_env_sensor.yaml"><img src="./img/living_room_env_sensor~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./living_room_ir_sensor.yaml"><img src="./img/living_room_ir_sensor.png" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./patio_floodlight.yaml"><img src="./img/patio_floodlight.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./slot_car_track.yaml"><img src="./img/slot_car_track.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./solar_hws_ctl.yaml"><img src="./img/solar_hws_ctl.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./solar_hws_ctl.yaml"><img src="./img/solar_hws_ctl~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./solar_hws_ctl.yaml"><img src="./img/solar_hws_ctl~3.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./studio_psu.yaml"><img src="./img/studio_psu.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./weather_oled.yaml"><img src="./img/weather_oled.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./wl_irrigation.yaml"><img src="./img/wl_irrigation.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./wl_irrigation.yaml"><img src="./img/wl_irrigation~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./wl_water_tank.yaml"><img src="./img/wl_water_tank.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./wl_water_tank.yaml"><img src="./img/wl_water_tank~2.jpg" style="max-width: 200px; max-height: 200px;"></td>
</tr>
<tr>
<td><a href="./wl_water_tank.yaml"><img src="./img/wl_water_tank~3.jpg" style="max-width: 200px; max-height: 200px;"></td>
<td><a href="./wl_water_tank.yaml"><img src="./img/wl_water_tank~4.jpg" style="max-width: 200px; max-height: 200px;"></td>
</table>

## Notes

### ESPHome

https://esphome.io/guides/getting_started_command_line.html

https://esphome.io/components/wifi.html

https://esphome.io/components/mqtt.html

https://www.home-assistant.io/docs/mqtt/discovery

https://www.home-assistant.io/components/esphome/

### Install

    pipenv install

    pipenv run esphome device_name.yaml run

### Wemos D1 Mini (ESP8266) v2.0.0

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
