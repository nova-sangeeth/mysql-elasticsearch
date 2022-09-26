import random
import string
from typing import List


def data_gen(limit: int) -> List:
    temp_data_store = []
    for i in range(limit):
        dictionary = {
            "id": i,
            "name": "".join(random.choices(string.ascii_letters, k=15)),
            "address": "".join(random.choices(string.ascii_letters, k=15)),
            "age": random.randint(a=10, b=99),
        }
        temp_data_store.append(dictionary)
    return temp_data_store


def data_gen_2(limit: int) -> List:
    temp_data_store = []
    for i in range(limit):
        dictionary = {
            "id": i,
            "name": "".join(random.choices(string.ascii_letters, k=15)),
            "address": "".join(random.choices(string.ascii_letters, k=15)),
            "age": random.randint(a=10, b=99),
            "phone": random.randint(a=8000000000, b=9000000000),
        }
        temp_data_store.append(dictionary)
    return temp_data_store
