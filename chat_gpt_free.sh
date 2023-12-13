#!/usr/local/bin/fish

set PATH_SCRIPT_DIR '/Users/sonic/PycharmProjects/chat_gpt_free/'
set PYTHON_BIN_VER python3.12

cd $PATH_SCRIPT_DIR
. venv/bin/activate.fish

clear

$PYTHON_BIN_VER main.py