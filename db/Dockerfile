FROM postgres:latest
ENV POSTGRES_PASSWORD=pass
ENV POSTGRES_USER=usr
ENV POSTGRES_DB=sqlalchemy

COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql

