from app.celery_holder import celery
from app.main.parse_csv import ParseCSV


@celery.task
def csv_pipeline(blob_url, delimiter, engine):
    parser = ParseCSV(
        blob_url,
        delimiter,
        engine
    )

    parser.execute()
