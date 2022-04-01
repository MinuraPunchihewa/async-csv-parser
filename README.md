# Asynchronous CSV Parser
This is a multi-container application that processes CSV files stored in Azure Blob Storage and dumps the data into a MariaDB database.

To perform asynchronous operations, a Celery worker has been integrated with a Redis queue. Any requests that are sent to the Web service will be stored in the Redis queue. The Celery worker will poll this queue and fulfill the requests in order.

This project can be easily converted to an application that processes other types of files, such as XML, Parquet etc., in an asynchronous manner or it can be used as a blueprint for any asynchronous Flask API.

## Run Locally

Clone the project,

```
git clone https://github.com/MinuraPunchihewa/async-csv-parser.git
```

Complete the `docker-compose.yml` file by filling in your database credentials. Add the relevant parameters to the `DB_HOST`, `DB_USER`, `DB_PASSWORD` and `DB_NAME` environment variables under both the `web` and `c_worker_01` containers.

Go to the project directory,

```
cd async-csv-parser
```

Build the Docker images,

```
docker-compose build
```

Run the application,

```
docker-compose up
```

Alternatively, combine the two commands above and run,

```
docker-compose build && docker-compose up
```

Submit a POST request to the `/parse-csv` endpoint along with the `blob_url` and the `delimiter` as form data,
```
localhost/parse-csv
```
The `blob_url` should be a Shared Access Signature (SAS) that is generated from your CSV file stored in Azure Blob Storage, while the delimiter/separator is the character that separates the data within the file.
