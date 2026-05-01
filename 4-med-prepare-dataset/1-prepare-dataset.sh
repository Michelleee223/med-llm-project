#!/bin/sh

## Download from https://gitee.com/songting/cMedQA2

unzip question.zip
unzip answer.zip

python prepare_dataset.py