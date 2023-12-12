python3 -m venv .venv
source .venv/bin/activate
pip install requests python-dotenv Flask
python -m pip install -U pip
pip freeze > requirements.txt
pip install waitress