
# Elasticsearch Project

This project sets up an Elasticsearch instance using Docker Compose, loads sample match data into Elasticsearch, and performs a full-text search using Python.

## Project Structure

```
elasticsearch_project/
│
├── docker-compose.yml    # Docker Compose configuration for Elasticsearch
├── data.json             # Sample data to be loaded into Elasticsearch
├── load_data.py          # Script to load data into Elasticsearch
├── search_data.py        # Script to perform a search in Elasticsearch
├── execute.sh            # Bash script to execute the whole process
└── requirements.txt      # Python dependencies
```

## How to Use

1. **Start Elasticsearch and Load Data**
    ```bash
    ./execute.sh
    ```

This script will:
- Start the Elasticsearch service with Docker Compose
- Activate the virtual environment and install dependencies
- Load data from `data.json` into Elasticsearch
- Perform a full-text search for matches including "England"
- Shut down the Elasticsearch service
