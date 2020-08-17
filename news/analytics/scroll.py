#! /usr/bin/env python

from elasticsearch import Elasticsearch
import json

# Define config
host = "127.0.0.1"
port = 9200
timeout = 1000
index = "news_data"
#doc_type = "type"
size = 1000
body = {}

# Init Elasticsearch instance
es = Elasticsearch(
    [
        {
            'host': host,
            'port': port
        }
    ],
    timeout=timeout
)


# Process hits here
def process_hits(hits):
    for item in hits:
        print(json.dumps(item, indent=2))
        exit()


# Check index exists
if not es.indices.exists(index=index):
    print("Index " + index + " not exists")
    exit()

# Init scroll by search
data = es.search(
    index=index,
    #doc_type=doc_type,
    scroll='2m',
    size=size,
    body=body
)

# Get the scroll ID
sid = data['_scroll_id']
scroll_size = len(data['hits']['hits'])

print(scroll_size)

#while scroll_size > 0:
#    "Scrolling..."
    
    # Before scroll, process current batch of hits
#    process_hits(data['hits']['hits'])
    
#    data = es.scroll(scroll_id=sid, scroll='2m')

    # Update the scroll ID
#    sid = data['_scroll_id']

    # Get the number of results that returned in the last scroll
#    scroll_size = len(data['hits']['hits'])

#print(scroll_size)
