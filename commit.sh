# BASH script for commiting code to PyPi

bash clean.sh
nano meraki_cli/__version__.py
python3 -m venv commit_env
source ./commit_env/bin/activate
python3 -m pip install --upgrade pip
pip3 install wheel
pip3 install twine
python3 setup.py sdist bdist_wheel
twine upload dist/*

read -p "Press ENTER to continue"


deactivate

bash clean.sh
