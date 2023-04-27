import csv
import sqlite3
from datetime import datetime

conexao = sqlite3.connect('radar.db')
cursor = conexao.cursor()

ticket = "ITSA3"

# Abrir o arquivo CSV
with open('ITSA3.SA.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    for linha in leitor_csv:
        coluna1 = linha[0]
        coluna2 = linha[1]
        coluna3 = linha[2]
        coluna4 = linha[3]
        coluna5 = linha[4]
        coluna6 = linha[5]
        coluna7 = linha[6]
        
        # Verificar se a variável coluna1 não está vazia
        if coluna1 and '-' in coluna1:
            ano, mes, dia = coluna1.split('-')
            data = datetime(int(ano), int(mes), int(dia))  # Substitua com a data desejada
            cursor.execute("INSERT INTO cotacao (simbolo, data, minima, maxima) VALUES (?, ?, ?, ?)", (ticket, data, coluna4, coluna3))
            conexao.commit()
        else:
            print("Erro: A coluna1 não possui o formato esperado.")
