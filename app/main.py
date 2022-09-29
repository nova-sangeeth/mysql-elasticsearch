from elasticsearch import Elasticsearch
from config import ELASTICSEARCH_HOST_URL

es_client = Elasticsearch(hosts=ELASTICSEARCH_HOST_URL)
