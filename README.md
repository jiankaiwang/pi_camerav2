# Applications on Pi Camera V2

![](https://img.shields.io/badge/Raspberry_Pi-3B-informational)
![](https://img.shields.io/badge/Pi_Camera-V2-informational)

## Environments

After setting up the Raspberry Pi Camera V2, you should setup the config on Pi. 
You can download the `raspi-config.deb` from the below link and install it download.

[http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/](http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/)

```sh
# install the dependencies
wget http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20200707_all.deb
sudo apt-get update
sudo apt-get install whiptail parted lua5.1 alsa-utils psmisc

# install the raspi-config
sudo dpkg -i raspi-config_20200707_all.deb
```

Run the following commands and enable all items under `5. Inferface Options` (or `3. Inferface Options`).

```sh
sudo raspi-config

# You can check the camera setting state.
#
# supported=1 detected=1 
vcgencmd get_camera
```

Click `finish` and `reboot` now.

## Quick Start

### Using the official tools

```sh
sudo apt install libraspberrypi-bin
```

Run the following commands to take capture.

```sh
raspistill -o ./image.jpg
```

### Using the Python Package `picamera`

[`Optional`] Install the dependencies and setup all configures. 

```sh
sudo apt-get install -y x11-common \
  libsm6 \
  libxtst6 \
  libice6 \
  libraspberrypi0 
wget https://archive.raspberrypi.org/debian/pool/main/r/realvnc-vnc/realvnc-vnc-server_6.7.2.43081_arm64.deb
sudo dpkg -i realvnc-vnc-server_6.7.2.43081_arm64.deb

cd /usr/lib/aarch64-linux-gnu/
sudo ln libvcos.so /usr/lib/libvcos.so.0
sudo ln libvchiq_arm.so /usr/lib/libvchiq_arm.so.0
sudo ln libbcm_host.so /usr/lib/libbcm_host.so.0

sudo systemctl enable vncserver-virtuald.service
sudo systemctl enable vncserver-x11-serviced.service
sudo systemctl start vncserver-virtuald.service
sudo systemctl start vncserver-x11-serviced.service

reboot
```

Create a python virtualenv for accessing the camera library.

```sh
python3 -m virtualenv -p python3 env
source ./env/bin/activate
pip3 install --no-cache-dir picamera
```

Run the following command to use the picamera library.

```sh
# for the image example
python3 ./picam/example.py --type=image --path=./image.jpg

# for the video example
python3 ./picam/example.py --type=video --path=./video.h264
```

Run the following command to test the `exposure` and `white balance`.
The `exposure` supports the following modes.

```text
off
auto
night
nightpreview
backlight
spotlight
sports
snow
beach
verylong
fixedfps
antishake
fireworks
```

The `white balance` supports the following modes.

```text
off
auto
sunlight
cloudy
shade
tungsten
fluorescent
incandescent
flash
horizon
```

Run the following script to test the parameters.

```sh
# auto 
python3 ./picam/parameters.py \
  --exposure=night \
  --awb=auto \
  --path=./image.jpg
```

### Using the OpenCV
