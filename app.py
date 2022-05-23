import pyodbc

#conectar com os dados no SQL

dados_conectados = (
        "Drive={SQL Server};"
        "Server=#;"
        "Database=ContosoRetailDW;"
)

conexao = pyodbc.connect(dados_conectados);
print('sucesso na conexão');
