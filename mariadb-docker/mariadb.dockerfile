FROM docker.io/bitnami/mariadb:10.8


COPY init-db.sql /docker-entrypoint-initdb.d/init_db.sql
