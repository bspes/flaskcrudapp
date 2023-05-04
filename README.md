FlaskCRUDapp
================

Prvotna inicializacia virtualenv
----------------
    python3 -m venv venv
    source venv/bin/activate
    git clone https://github.com/bspes/flaskcrudapp.git
    cd flaskcrudapp
    pip install -r requirements.txt
Nasledne je potrebne zmenit cestu v instance/config.py a test.py k databaze

Inicializacia virtualenv pre vyvoj
----------------
    source venv/bin/activate

Spustenie app v devel mode
----------------
    export FLASK_CONFIG=development
    export FLASK_APP=run.py
    flask run
