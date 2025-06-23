#! /usr/bin/bash

echo Installing Fieldstation 42 Numpad Control

echo Finding python installation...
python=python3

if type "python3" > /dev/null; then
    echo "Found python3 - using that"
    python=python3
elif type "python" > /dev/null; then
    echo "Found python - using that"
    python=python
else
    echo ERROR :: Couldn\'t find python or python3 on the path
    echo Please install python and try again
    exit -1
fi

echo Moving forward with python :: $python
echo Creating python virtual environment

if [ -f /.dockerenv ]; then
  echo "Running inside Docker — skipping venv setup."

else
  $python -m venv env
  # do your venv setup
  if [ -d env ]; then

    echo Virtual environment created - activating it now
    # Unix
    if [ -f env/Scripts/activate ]; then
      source env/Scripts/activate
    # Windows
    elif [ -f env/bin/activate ]; then
      source env/bin/activate
    else
      echo Virtual environment does not contain activate script - this is an error
      echo Ensure that python3-venv is installed and run the installer again.
      exit -1
    fi
  else
    echo Virtual environment failed - check that your python venv is installed on your system
    echo Exiting with errors.
    exit -1
  fi
fi

echo Installing python modules
pip install -r requirements.txt

echo Installation is complete
