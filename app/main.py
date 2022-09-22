from elasticsearch import Elasticsearch
from typing import List

URL = "http://localhost:9200"


client = Elasticsearch(URL)


input_query_string = input("Enter the query: ")

print(
    f"""

{client.info()}


"""
)

# query_body = {"query": {"match": {"client_name": "two"}}}


def search_queries(index_name: str, query_string: str) -> List:
    search_response = client.search(
        index=index_name, query={"match": {"client_name": query_string}}
    )

    results = []

    for i in search_response["hits"]["hits"]:
        dictionary = {
            "id: " + str(i["_source"]["id"]),
            "client_name: " + i["_source"]["client_name"],
            "modification_time: " + i["_source"]["modification_time"],
        }

        results.append(dictionary)

    return results


values = search_queries(index_name="test-idx-2", query_string=input_query_string)

print(values)
