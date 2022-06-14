# import the main blue print instance
from app.main import main
from app.main.celery_tasks import csv_pipeline
from flask import request, jsonify, abort
from flask import current_app
import logging


@main.route('/parse-csv', methods=['POST'])
def parse_csv():
    blob_url = request.form.get('blob_url')
    delimiter = request.form.get('delimiter')

    try:
        csv_pipeline.delay(blob_url, delimiter, current_app.config["SQLALCHEMY_DATABASE_URI"])
    except Exception as err:
        logging.error(f"{err} getting task.")
        return 'Failed to que task'

    return 'Task queued: CSV parser.'
