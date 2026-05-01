#!/bin/sh


# https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt_tab.zip

uv tool install vllm==0.11.2

uv run install_nltk_data.py