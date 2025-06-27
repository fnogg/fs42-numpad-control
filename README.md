# FieldStation42 Numpad Control

This is designed to be used with [FieldStation42](https://github.com/shane-mason/FieldStation42). It provides functionality to capture numpad input from a keyboard or numpad device, and translate it into controls for changing the channels on a FieldStation42 instance running on the same device.

## Installation & setup

### 1. Clone this repo

`git clone github.com/fnogg/fs42-numpad-control`

`cd fs42-numpad-control`

### 2. Install dependencies

If you already have FieldStation42 running, you should already have Python ready to go. You should only need to run:

`bash install.sh`

This will install a python virtual environment (required on Raspian), and install python dependencies.

### 3. Configuration

Copy `.env.example` to `.env`, then edit the values in `.env` as needed to configure for your setup. On a Raspberry Pi, the input device can generally be identified by looking at the output of `cat /proc/bus/input/devices` - more information on this can be found on [this blog post - DYI Macro Keyboard on Linux](https://blog.luk.world/posts/dyi-macro-keyboard-on-linux-elgato-stream-deck/).

## Usage

Note before running the script that it will take over all input from the configured device. This means you won't be able to exit the script using the same keyboard, so use with caution if you don't have another input method or ssh connection available.

To start the script:

`cd ~/fs42-numpad-control`

`source env/bin/activate`

`python3 fs42-numpad-control.py`

## Auto start

Copy `fs42_numpad_control_hot_start.sh` as needed into your method of choice for auto-starting the script on startup. Some options include:
[FieldStation42 - Autostart on Raspberry Pi](https://github.com/shane-mason/FieldStation42/wiki/Autostart-on-Rasberry-Pi)

If running on Raspbian Lite, options that require a desktop environment will not work. You can also add the hot start script to `/etc/profile.d` to have it run on login, but note that it will start up a new instance on EACH login (local + ssh for example).
