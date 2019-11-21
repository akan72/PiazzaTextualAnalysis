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

# Install Python package requirements
pip install -r requirements.txt

# Run the jupyter notebook pipeline
# jupyter nbconvert --to notebook --inplace --execute --ExecutePreprocessor.timeout=300 pickle_posts.ipynb
# jupyter nbconvert --to notebook --inplace --execute --ExecutePreprocessor.timeout=300 transform_posts.ipynb
