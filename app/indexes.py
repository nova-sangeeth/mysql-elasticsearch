# example index structure

"""
my_index_schema = {
    "mappings": {
        "properties": {
            "field": {"type": "text"},
            "field": {"type": "integer"},
        }
    }
}

NO SUPPORT FOR ARRAY FIELDS.
"""


index_schema_1 = {
    "mappings": {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "text"},
            "address": {"type": "text"},
            "age": {"type": "integer"},
        }
    }
}


index_schema_2 = {
    "mappings": {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "text"},
            "address": {"type": "text"},
            "age": {"type": "integer"},
            "phone_number": {"type": "integer"},
        }
    }
}
