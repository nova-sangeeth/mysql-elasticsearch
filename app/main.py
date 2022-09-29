from elasticsearch import Elasticsearch
from config import ELASTICSEARCH_HOST_URL, DEBUG
from flask import Flask

app = Flask(__name__)
es_client = Elasticsearch(hosts=ELASTICSEARCH_HOST_URL)


@app.route("/")
def home():
    message = {"message": "App works."}
    return message


if __name__ == "__main__":
    app.run(debug=DEBUG)
