FlaskCRUDapp
================

Prvotna inicializacia virtualenv
----------------
    source /home/bodo/.local/bin/virtualenvwrapper.sh
    export WORKON_HOME=~/Envs
    mkvirtualenv flask-env
    workon flask-venv
    git clone https://github.com/bspes/flaskcrudapp.git
    cd flaskcrudapp
    pip install -r requirements.txt

Inicializacia virtualenv pre vyvoj
----------------
    source /home/bodo/.local/bin/virtualenvwrapper.sh
    export WORKON_HOME=~/Envs
    workon flask-venv

Spustenie app v devel mode
----------------
    export FLASK_CONFIG=development
    export FLASK_APP=run.py
    flask run
