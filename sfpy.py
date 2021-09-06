import snowflake.connector
import pandas as pd


class SfOnPy(object):

    def __init__(self, user, password, account, warehouse=None, database=None):
        self.__user = user
        self.__password = password
        self.__account = account
        self.__warehouse = warehouse
        self.__database = database

    def __start(self):
        connection = snowflake.connector.connect(
            user=self.__user,
            password=self.__password,
            account=self.__account,
            warehouse=self.__warehouse,
            database=self.__database
        )
        
        cursor = connection.cursor()

        return cursor

    def __pure_query(self, sql):
        raw_query_split = sql.split('\n')

        wo_linebreak = []
        for items in raw_query_split:
            wo_linebreak += items.split(' ')

        pure = [chunk for chunk in wo_linebreak if chunk != '']
        query = ' '.join(pure)

        return query

    def query_result(self, sql, size='all'):
        cursor = self.__start()
        query = self.__pure_query(sql)

        if size == 'all':
            cursor.execute(query)
            df = cursor.fetch_pandas_all()
            cols = [col.lower() for col in list(df.columns)]
            df.columns = cols

        else:
            colnames = [item.name.lower() for item in cursor.describe(query)]
            df = pd.DataFrame(columns=colnames)
            cursor.execute(query)

            if size == 1:
                batchone = cursor.fetchone()
                for i in range(len(colnames)):
                    idx = colnames[i]
                    df[idx] = [batchone[i]]

            else:
                batchmany = cursor.fetchmany(size=size)
                for i in range(len(colnames)):
                    ith = [tup[i] for tup in batchmany]
                    idx = colnames[i]
                    df[idx] = ith

        return df