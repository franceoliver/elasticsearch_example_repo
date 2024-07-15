import json
import requests

# Define the Elasticsearch endpoint
ES_ENDPOINT = "http://localhost:9200"
INDEX_NAME = "matches"

# Search data in Elasticsearch
def search_data(query):
    search_query = {
        "query": {
            "match": {
                "result": query
            }
        },
        "sort": [
            {"date": {"order": "asc"}}
        ]
    }
    response = requests.get(f"{ES_ENDPOINT}/{INDEX_NAME}/_search", headers={"Content-Type": "application/json"}, data=json.dumps(search_query))
    print("Search results:")
    results = response.json()
    for hit in results['hits']['hits']:
        match = hit['_source']
        print(json.dumps(match, indent=4, sort_keys=True))

if __name__ == "__main__":
    search_data("England")
