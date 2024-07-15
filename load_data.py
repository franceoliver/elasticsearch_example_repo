import json
import requests

# Define the Elasticsearch endpoint
ES_ENDPOINT = "http://localhost:9200"
INDEX_NAME = "matches"

# Create the index
def create_index():
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "match_id": {"type": "integer"},
                "match_type": {"type": "text"},
                "teams": {"type": "keyword"},
                "date": {"type": "date"},
                "venue": {"type": "text"},
                "odds": {
                    "properties": {
                        "team_1": {"type": "float"},
                        "team_2": {"type": "float"}
                    }
                },
                "result": {"type": "text"}
            }
        }
    }
    response = requests.put(f"{ES_ENDPOINT}/{INDEX_NAME}", headers={"Content-Type": "application/json"}, data=json.dumps(index_settings))
    print(f"Index creation response: {response.json()}")

# Load data from JSON file
def load_data():
    with open("data.json") as f:
        matches = json.load(f)
        for match in matches:
            response = requests.post(f"{ES_ENDPOINT}/{INDEX_NAME}/_doc/{match['match_id']}", headers={"Content-Type": "application/json"}, data=json.dumps(match))
            print(f"Document {match['match_id']} creation response: {response.json()}")

if __name__ == "__main__":
    create_index()
    load_data()
