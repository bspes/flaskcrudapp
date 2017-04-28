flaskcrudapp
================

Prvotna inicializacia virtualenv
----------------
    source /home/bodo/.local/bin/virtualenvwrapper.sh
    export WORKON_HOME=~/Envs
    mkvirtualenv my-venv

Inicializacia virtualenv pre vyvoj
----------------
    source /home/bodo/.local/bin/virtualenvwrapper.sh
    export WORKON_HOME=~/Envs
    workon my-venv

Spustenie app v devel mode
----------------
    export FLASK_CONFIG=development
    export FLASK_APP=run.py
    flask run
