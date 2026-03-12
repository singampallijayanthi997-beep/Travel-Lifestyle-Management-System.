import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayanthi@9",
        database="travel_lifestyle"
    )
    return connection