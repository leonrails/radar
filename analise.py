import sqlite3
import sys
import os



# Conectar ao banco de dados
conexao = sqlite3.connect('radar.db')
cursor = conexao.cursor()

os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o menu
def exibir_menu():
    print("===== MENU =====")
    print("1. Listar tickets'")
    print("2. Inserir ticket")
    print("3. Inserir cotação diária")
    print("0. Sair")

# Loop principal do programa
while True:
    exibir_menu()
    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        print("Você selecionou a Opção 1.")
        # Coloque o código da Opção 1 aqui
        cursor.execute("SELECT * FROM ticket")
        resultados = cursor.fetchall()
        # Exibir resultados na tela
        if resultados:
            print("\n==Resultados da consulta==\n")
            print("{:<10} {:<10}".format("Simbolo", "Empresa"))
            print("-" * 20)  # Linha separadora
            for linha in resultados:
                print("{:<10} {:<10}".format(linha[0], linha[1]))
        print("\n\n\n")

    elif escolha == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("== Insira as Informações ==\n")
        # Coloque o código da Opção 2 aqui
        ticket = input("Digite o ticket....: ")
        empresa = input("Nome Empresa.......: ")
        ticket = ticket.upper()
        try:
            # Executar a inserção
            cursor.execute("INSERT INTO ticket (simbolo, empresa) VALUES (?, ?)", (ticket, empresa))
            # Confirmar a transação
            conexao.commit()
            print("Dados inseridos com sucesso!")
        except sqlite3.Error as erro:
            print("Erro ao inserir dados:", erro)

    elif escolha == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("== Insira as Informações ==\n")
        # Coloque o código da Opção 2 aqui
        ticket = input("Digite o ticket....: ")
        data = input("Data (dd/mm/aaaa)..: ")
        minima = int(input("Cotação mínima.....: "))
        maxima = int(input("Cotação máxima.....: "))
        try:
            # Dados a serem inseridos
            dados = ('ITSA',)  # Valor a ser inserido no campo VARCHAR de 5 caracteres
            # Executar a inserção
            cursor.execute("INSERT INTO ticket (campo_varchar) VALUES (?)", dados)
            # Confirmar a transação
            conexao.commit()
            print("Dados inseridos com sucesso!")
        except sqlite3.Error as erro:
            print("Erro ao inserir dados:", erro)

    elif escolha == "0":
        print("Bons Negócios!!!\n\n")
        conexao.close()
        break  # Sai do loop e encerra o programa

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

