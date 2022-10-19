from http import client
from elasticsearch import Elasticsearch

from typing import List
from config import HOST_URL
from elasticsearch_dsl import Search

es_client = Elasticsearch(HOST_URL)

query_body = {"query": {"match": {"client_name": "two"}}}


def search_queries(index_name: str, query_string: str) -> List:
    search_response = es_client.search(
        index=index_name,
        query={"term": {"age": query_string}}
        # index=index_name, query={"match": {"name": query_string}}
    )

    results = []

    for i in search_response["hits"]["hits"]:

        results.append(i)

    return {"count": len(results), "respose_data": results}


values = search_queries(index_name="my_index", query_string="78")

print(values)


# Generate data -
# Push to logstash X
# Learn how ElasticSearch Works
