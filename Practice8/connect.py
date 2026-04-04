import psycopg2
from config import host, port, database, user, password

def connect():
    connection = None 
    try:   
        connection = psycopg2.connect(
            host=host, 
            user=user, 
            password=password, 
            database=database, 
            port=port
        ) 
    except Exception as ex:
        print("Соединение не установлено...") 
        print(ex)
    
    return connection