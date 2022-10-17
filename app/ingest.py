import time
from db import Session
from main import es_client
from sqla_es import Elasticsearch
from data_generator import data_gen, data_gen_2

es_client.ping(pretty=True)

session = Session()


def ingest(
    index_name_1: str,
    index_name_2: str,
    data_gen_count: int,
    iteration: int,
    iteration_limit: int,
    sleep_time: int,
) -> str:

    while iteration != iteration_limit:
        iteration += 1
        time.sleep(sleep_time)
        # ceate dummy  data
        data_1 = data_gen(limit=data_gen_count)
        data_2 = data_gen_2(limit=data_gen_count)

        # insert data into the created indexes.

        for doc in data_1:
            print(doc)
            ingest = es_client.index(index=index_name_1, document=doc)
            print(ingest)

        for doc in data_2:
            print(doc)
            ingest = es_client.index(index=index_name_2, document=doc)
            print(ingest)

    message = f"Data Ingestion Complete after {iteration_limit} iterations"
    return message


# ingest(
#     index_name_1="my_index_1",
#     index_name_2="my_index_2",
#     data_gen_count=100,
#     iteration=0,
#     iteration_limit=5,
#     sleep_time=3,
# )


def ingest_from_db(db_session: session, index_name_1: str):
    query = db_session.query(Elasticsearch)
    data = [row.__dict__ for row in query.all()]
    for doc in data:
        del doc["_sa_instance_state"]
        ingest = es_client.index(index=index_name_1, document=doc)
        print(ingest)


ingest_from_db(session, index_name_1="my_index_1")
