# Set ip virtual environment
python3 -m venv .venv
# enter virtual environment
source .venv/bin/activate
# install pip
pip install requests python-dotenv Flask
python -m pip install -U pip
# install waitress
pip freeze > requirements.txt
pip install waitress

# Start server
python3 server.py