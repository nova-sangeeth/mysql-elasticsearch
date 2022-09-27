from elasticsearch import Elasticsearch
from data_generator import data_gen, data_gen_2
from indexes import index_schema_1, index_schema_2
from config import HOST_URL
import time

from main import es_client

index_name_1 = "my_index_1"
index_name_2 = "my_index_2"

iteration = 0
limit = 5
sleep_time = 3

while iteration != limit:
    iteration += 1
    time.sleep(sleep_time)
    # temporary data
    data_1 = data_gen(limit=500)
    data_2 = data_gen_2(limit=500)

    # insert data into the created indexes.

    for document in data_1:
        es_client.index(index=index_name_1, body=document)

    for document in data_2:
        es_client.index(index=index_name_2, body=document)


print(f"Data Ingestion Complete after {limit} iterations")
