FlaskCRUDapp
================

Prvotna inicializacia
----------------
    python3 -m venv venv
    source venv/bin/activate
    git clone https://github.com/bspes/flaskcrudapp.git
    cd flaskcrudapp
    pip install -r requirements.txt
    #edituj SECRET_KEY v instance/config.py
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    #edituj create_admin_user.py, daj tam email a heslo co pouzijes
    python3 create_admin_user.py

Inicializacia virtualenv pre vyvoj
----------------
    source venv/bin/activate

Spustenie app v devel mode
----------------
    export FLASK_CONFIG=development
    export FLASK_APP=run.py
    flask run
