import json
import os
from evdev import InputDevice, categorize, ecodes
from dotenv import load_dotenv, dotenv_values
load_dotenv()

channel_socket = os.getenv("FS42_CHANNEL_SOCKET_PATH")
dev = InputDevice(os.getenv("INPUT_DEVICE"))
dev.grab()

input_buffer = ""

def send_command(command, channel = -1):
  command_obj = {'"command"': command, '"channel"': channel}
  os.system('echo ' + json.dumps(command_obj))
  os.system('echo ' + json.dumps(command_obj) + ' > ' + channel_socket)

for event in dev.read_loop():
  if event.type == ecodes.EV_KEY:
    key = categorize(event)
    if key.keystate == key.key_down:
      # When a keypad number is pressed, add the number to the input buffer
      if key.keycode.startswith('KEY_KP') and key.keycode[-1].isdigit():
        input_buffer += key.keycode[-1]
      # When keypad enter is pressed, send the contents of the input buffer
      # as a channel number and clear the input buffer
      if key.keycode == 'KEY_KPENTER' and input_buffer.isnumeric():
        os.system('echo Changing to channel: ' + input_buffer)
        send_command('"direct"', int(input_buffer))
        input_buffer = ""
      # Plus button turns the channel up 1
      if key.keycode == 'KEY_KPPLUS':
        send_command('"up"')
      # Minus button turns the channel down 1
      if key.keycode == 'KEY_KPMINUS':
        send_command('"down"')