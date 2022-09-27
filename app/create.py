from elasticsearch import Elasticsearch
from data_generator import data_gen, data_gen_2
from indexes import index_schema_1, index_schema_2
from config import HOST_URL
import time
# create a new elasticsearch client
from main import es_client
# index_names
index_name_1 = "my_index_1"
index_name_2 = "my_index_2"
index_name_3 = "my_index_2"

# create new indexes
es_client.indices.create(index=index_name_1, body=index_schema_1)
es_client.indices.create(index=index_name_2, body=index_schema_2)
# es_client.indices.create(index=index_name_3, body=index_schema_2)
