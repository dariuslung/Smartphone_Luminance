![smartphone_interface_cropped](https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/58188bf5-5ac7-48a5-a016-d6cfa0e90ca2)# Smartphone_Luminance
Modified from [Smartphone_v1_WebVersion](https://github.com/tsaiwn/Smartphone_v1_WebVersion/)

Automatically binds with IoTTalk device dzo_smartphone
IDF: Acceleration, Illuminance

## Tutorial
1. To get this working on Chrome Android, proceed to `chrome://flags` and set `#enable-generic-sensor-extra-classes` to `Enabled`.
This is required for `AmbientLightSensor` as it is still an experimental web API.
2. `app.py` requires the Python package Flask, install it with `pip install Flask`.
3. Start the server by with `python app.py`.

![image](https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/cef722c9-c503-428d-a8d5-84a548eb684f)

5. Observe the IP it is running on.
If your smartphone is connected to the same network as your server is running on, connect to `https://xxx.xxx.xxx.xxx/` in Chrome Android and bypass the safety warning.

![smartphone_interface_cropped](https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/17a9d0ed-fb57-4b8e-ae81-6042dabc03d6)

6. Proceed to https://2.iottalk.tw/ and have fun with your project~

![iottalk_luminance](https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/24068c9b-9b10-41e8-af40-e5021b01c513)
