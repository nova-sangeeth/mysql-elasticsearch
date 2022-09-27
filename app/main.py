from elasticsearch import Elasticsearch
from config import HOST_URL


es_client = Elasticsearch(
    hosts=HOST_URL,
)
