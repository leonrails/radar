import sqlite3
import sys
import os



# Conectar ao banco de dados
conexao = sqlite3.connect('radar.db')
cursor = conexao.cursor()

os.system('cls' if os.name == 'nt' else 'clear')

cursor.execute("SELECT a.Date AS 'Dia',a.High AS 'MAX 3',b.High AS 'MAX 4',a.High-b.High AS 'Dif' FROM IITSA3 a, IITSA4 b WHERE date(a.Date) = date(b.Date) ORDER BY a.Date DESC;")
resultados = cursor.fetchall()
# Exibir resultados na tela
if resultados:
    print("\n==Resultados da consulta==\n")
    print("{:<10} {:<10}".format("Data", "MAX 3", "MAX 4"))
    print("-" * 20)  # Linha separadora
    for linha in resultados:
        print("{:<10} {:<10}".format(linha[0], linha[1]), linha[2], linha[3])
print("\n\n\n")

