import pandas as pd
from src.conf import configuration
from src.model import embedding


def pgv_read(query):

    conn = configuration.pgv_connection
    cursor = conn.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    # Get column names
    col_list = [desc[0] for desc in cursor.description]

    # Create DataFrame
    df = pd.DataFrame(rows, columns=col_list)

    # Close the cursor and connection
    cursor.close()

    return df

def pgv_truncate(schema_name,table_name):

    conn = configuration.pgv_connection
    cursor = conn.cursor()
    cursor.execute(f"""DELETE FROM {schema_name}.{table_name} where 1 = 1  """)
    conn.commit()

def pgv_insert(df,schema_name,table_name):
    '''
    df = shared.pgv_read('select * from public.test')
    :param df: Pandas DataFrame which needs to be inserted.Make sure column name in the dataframe is same as the table
    :param schema_name: table schema in Postgre
    :param table_name: table name
    :return: NA
    '''

    conn = configuration.pgv_connection
    cursor = conn.cursor()

    columns = ', '.join(df.columns)
    values = ', '.join(['%s'] * len(df.columns))

    for index, row in df.iterrows():
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES ({values})",
            tuple(row)
        )
        conn.commit()


    # Close the cursor and connection
    cursor.close()

def pgv_semantic_search(user_input,schema_name,table_name,embedding_field):

    conn = configuration.pgv_connection
    cursor = conn.cursor()

    user_input_embedding = embedding.get_embeddings(user_input)
    search_query = f"""select *, 1 - ({embedding_field} <=> '{user_input_embedding}') as distance from {schema_name}.{table_name} order by {embedding_field} <=> '{user_input_embedding}' LIMIT 5;"""

    cursor.execute(search_query)

    rows = cursor.fetchall()

    # Get column names
    col_list = [desc[0] for desc in cursor.description]

    # Create DataFrame
    df = pd.DataFrame(rows, columns=col_list)


    # Close the cursor and connection
    cursor.close()
    return df


