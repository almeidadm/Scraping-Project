import sqlite3


class DataFrameDB():

    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def fetch_data(self, query, params=()):
        self.connection.execute(query, params)
        return self.connection.fetchall()

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS data (
            title TEXT,
            price FLOAT,
            url TEXT,
            store TEXT
        )
        '''
        self.connection.execute(query)
        self.connection.commit()

    def insert_data(self, data_frame):
        data_frame.to_sql('data', self.connection, if_exists='replace', index=False)

    def save_dataframe(self, data_frame):
        self.connect()
        self.create_table()
        self.insert_data(data_frame)
        self.disconnect()

