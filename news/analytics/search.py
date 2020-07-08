#! /usr/bin/env python

from elasticsearch import Elasticsearch

es = Elasticsearch()

body1 = {
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "publishedat" : {
                            "gt" : "now-30d",
                            "lt" : "now"      
                        }
                    }
                },
                {
                    "match": {
                        "location": "United States",
                    }
                },
                {
                    "match": {
                        "news_type": "headlines",
                    }
                }
            ]
        }
    }
}


body2 = {
    "aggs": {
            "type_count": {
            "cardinality": {
            "field": "author.keyword"
             }
           }
       },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "publishedat" : {
                            "gt" : "now-30d",
                            "lt" : "now"      
                        }
                    }
                },
                {
                    "match": {
                        "location": "South Africa",
                    }
                },
                {
                    "match": {
                        "news_type": "headlines",
                    }
                }
            ]
        }
    }   

}

body3 = {
    "aggs": {
            "type_count": {
            "cardinality": {
            "field": "source.keyword"
             }
           }
       },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "publishedat" : {
                            "gt" : "now-30d",
                            "lt" : "now"      
                        }
                    }
                },
                {
                    "match": {
                        "location": "South Africa",
                    }
                },
                {
                    "match": {
                        "news_type": "headlines",
                    }
                }
            ]
        }
    }   

}


res1 = es.search(index="news_data", body=body1)
res2 = es.search(index="news_data", body=body2)
res3 = es.search(index="news_data", body=body3)

total_titles = res1['hits']['total']['value']
total_authors = res2['aggregations']['type_count']['value']
total_sources = res3['aggregations']['type_count']['value']


print(total_titles)
print(total_authors)
print(total_sources)
    
    