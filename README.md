# Smartphone_Luminance
Modified from [Smartphone_v1_WebVersion](https://github.com/tsaiwn/Smartphone_v1_WebVersion/)

Automatically binds with IoTTalk device dzo_smartphone

## Tutorial
1. To get this working on Chrome Android, proceed to `chrome://flags` and set `#enable-generic-sensor-extra-classes` to `Enabled`.
This is required for AmbientLightSensor as it is still an experimental web API.
2. app.py requires the Python package Flask, install it with `pip install Flask`.
3. Start the server with `python app.py`.

<div><img src="https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/26c9909e-a773-49fb-b4eb-ae429ae4d5f5" width=500></div>

4. Observe the IP it is running on.
If your smartphone is connected to the same network as your server is running on, connect to `https://xxx.xxx.xxx.xxx/` in Chrome Android and bypass the safety warning.

<div><img src="https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/17a9d0ed-fb57-4b8e-ae81-6042dabc03d6" width=500></div>

5. Proceed to https://2.iottalk.tw/ and have fun with your project~

<div><img src="https://github.com/dariuslung/Smartphone_Luminance/assets/90674518/24068c9b-9b10-41e8-af40-e5021b01c513" width=500></div>
