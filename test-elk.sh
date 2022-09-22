echo "

list of indexes

"
curl 'http://localhost:9200/_cat/indices'

echo "

query values from index 2

"
# curl 'http://localhost:9200/test-idx-2/_search?q=fiv*'

curl -X GET \
    http://localhost:9200/test-idx-2/_search \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/json' \
    -d '{
"query":
    {
        "match":
            {
                "client_name": "phrase"
            }
    }
}'
