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

    
    cursor = conn.cursor()  
    

    # Comando BULK INSERT
    comando = """BULK INSERT dbo.InventarioProduto
FROM 'Inserir_dados.csv'
WITH (
    FIELDTERMINATOR = ',',   
);"""
    
    cursor.execute(comando)
    

    print("Comando BULK INSERT executado com sucesso!")

    # Fechar o cursor e a conexão
    #cursor.close()
    #conn.close()
   # print("Conexão encerrada.")
    
except Exception as e:
    print("Erro ao conectar ao banco:", e)
