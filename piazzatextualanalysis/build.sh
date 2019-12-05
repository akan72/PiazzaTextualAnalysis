#!/bin/bash

# Check to see if the two Piazza login environment variables are set
if [[ -z "${PIAZZA_EMAIL}" ]]; then
	echo "PIAZZA_EMAIL is not set!"
	exit 1
fi

if [[ -z "${PIAZZA_PASSWORD}" ]]; then
    echo "PIAZZA_PASSWORD is not set!"
	exit 1
fi

mkdir data data/posts data/dataframes

# Install Python package requirements
python -m pip install -r requirements.txt

# Run the jupyter notebook pipeline
if [ ! "$(ls -A data/dataframes)" ]; then
	# jupyter nbconvert --to notebook --inplace --execute --ExecutePreprocessor.timeout=300 pickle_posts.ipynb
	# jupyter nbconvert --to notebook --inplace --execute --ExecutePreprocessor.timeout=300 transform_posts.ipynb
	python pickle_posts.py
	python transform_posts.py
fi 

# Run data analysis script and output plots
