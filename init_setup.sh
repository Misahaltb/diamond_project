#!/bin/bash

echo "$(date): START"
echo "$(date): Creating conda environment 'diomon_env' with Python 3.12.4"
conda create --prefix ./envs/diomon_env python=3.12.4 -y 

echo "$(date): Activating the environment"
source activate ./envs/diomon_env

pip install -r requirements.txt

echo "$(date): Environment 'diomon_env' setup completed"
 