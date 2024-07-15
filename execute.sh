#!/bin/bash

# Start Elasticsearch service with Docker Compose
echo "Starting Elasticsearch service with Docker Compose..."
docker-compose down
docker-compose up -d
echo "Waiting for Elasticsearch to start..."
sleep 30  # Wait for 30 seconds to ensure Elasticsearch is fully started

# Install the required Python packages
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run the script to load data into Elasticsearch
echo "Loading data into Elasticsearch..."
python load_data.py

# Run the script to perform a search in Elasticsearch
echo "Performing search in Elasticsearch..."
python search_data.py

echo "Execution completed."
