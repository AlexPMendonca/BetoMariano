import pyodbc
import pandas as pd


# Conexão
server = r'DESKTOP-8OJ2KUR\SQLEXPRESS'  
database = r'CANACOLETA_2024'
username = 'sa'
password = 'spark'

try:
    # Conecta SQL Server
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    print("Conexão bem-sucedida!")

    # Consulta
    cursor = conn.cursor()

    comando = """SELECT * FROM dbo.InventarioProduto"""

    cursor.execute(comando)

    cursor.commit()

    # Fecha
    #conn.close()
    #print("Conexão encerrada.")
except Exception as e:
    print("Erro ao conectar ao banco:", e)
