from elasticsearch import Elasticsearch
from data_generator import data_gen, data_gen_2
from indexes import index_schema_1, index_schema_2
from config import HOST_URL
import time

from main import es_client

index_name_1 = "my_index_1"
index_name_2 = "my_index_2"

test = True

while test:

    time.sleep(5)
    # temporary data
    data_1 = data_gen(limit=500)
    data_2 = data_gen_2(limit=500)

    # insert data into the created indexes.

    for document in data_1:
        es_client.index(index=index_name_1, body=document)

    for document in data_2:
        es_client.index(index=index_name_2, body=document)
