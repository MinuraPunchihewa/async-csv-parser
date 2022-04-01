import numpy as np
import pandas as pd
from azure.storage.blob import BlobClient
from io import BytesIO
import sqlalchemy
import logging


class ParseCSV:
    def __init__(self, blob_url, delimiter, database_uri):
        self.blobclient = BlobClient.from_blob_url(blob_url)
        self.file_name = self.blobclient.get_blob_properties()['name'].split('.')[0].lower()
        self.delimiter = delimiter
        self.engine = sqlalchemy.create_engine(database_uri, pool_pre_ping=True)

    def execute(self):
        try:
            # extract data
            df = self.__extract()

            # transform and load data
            self.__transform_and_load(df)
        except Exception as e:
            logging.error(e)

    def __extract(self):
        try:
            data = self.blobclient.download_blob()
            df = pd.read_csv(BytesIO(data.readall()), sep=self.delimiter)

            logging.info("Data successfully extracted")

            return df
        except Exception as e:
            logging.error(e)

    def __transform_and_load(self, df):
        # convert nan to None
        df = df.replace({np.nan: None})

        df.to_sql(con=self.engine, index=False, name=self.file_name, if_exists='append')
        logging.info("%s records inserted successfully into the %s table", len(df.index), self.file_name)
