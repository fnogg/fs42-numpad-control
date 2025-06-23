#/usr/bin/bash

cd ~/fs42-numpad-control
. env/bin/activate
python3 fs42-numpad-control.py 1>/dev/null 2>/dev/null & disown