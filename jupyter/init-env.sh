#!/usr/bin/env bash

pipenv install \
    notebook \
    jupyter_contrib_nbextensions \
    yapf \
    isort \
    autopep8 \
    numpy \
    pandas \
    seaborn \
    matplotlib

pipenv run jupyter contrib nbextension install --user
pipenv run jupyter nbextension enable code_prettify/code_prettify
pipenv run jupyter nbextension enable code_prettify/isort
pipenv run jupyter nbextension enable toggle_all_line_numbers/main
pipenv run jupyter nbextension enable comment-uncomment/main
