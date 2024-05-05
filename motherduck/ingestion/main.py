import loguru
from utils.functions import * 

logger = loguru.logger

def main():
    try:
        logger.info('Criando conexão com o MotherDuck')
        conn = create_connection()

        abs_path = abspath('motherduck/data/')
        tables = csv_names(abs_path)

        logger.info('Criando database motherduck')
        query_create_schema = read_sql_file(abspath('motherduck/ingestion/sql/create_database.sql'))
        execute_query(conn, query_create_schema)
        
        for table in tables:
            logger.info(f'Criando a tabela {table}')
            query_create_table = read_sql_file(abspath('motherduck/ingestion/sql/create_table.sql'), table=table.replace('.csv',''), abs_path=abs_path)
            execute_query(conn, query_create_table)

        tables_created = execute_query(conn, """
                                SELECT table_name
                                FROM information_schema.tables 
                                WHERE table_catalog = 'coffee_shop';""")
        
        logger.info(f'Tabelas criadas com sucesso: \n{tables_created}')

    except Exception as e:
        logger.error(f'Erro: {e}')

if __name__ == '__main__':
    main()
    