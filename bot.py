import sqlite3
import sys
import os
import locale 

# Conectar ao banco de dados
conexao = sqlite3.connect('radar.db')
cursor = conexao.cursor()

os.system('cls' if os.name == 'nt' else 'clear')

#Funcao consulta lista tickers dentro **Preco Teto**
#def dentro_pt():

#Funcao consulta lista tickers dentro **Preco Teto**
def painel(stock):
    cursor.execute("SELECT * FROM ticket WHERE simbolo = ?", (stock,))
    resultados = cursor.fetchall()
    if resultados:
        print("\n==Resultados da consulta==\n")
        print("{:<10} {:<10}".format("Simbolo", "Empresa"))
        print("-" * 20)  # Linha separadora
        for linha in resultados:
            #print("{:<10} {:<10}".format(linha[0], linha[1]))
            simbolo = linha[0]
            empresa = linha[1]
            tipo_acao = linha[2]
            composicao = linha[3]
            perc_payout_estatuto = linha[4]
            dy_med_trien = linha[5]
            preco_atual = linha[6]
            qtd_meta = linha[7]
            qtd_autal = linha[8]
            vl_investido = linha[9]
            previsao_receber = linha[10]
            patri_liq_antes = linha[11]
            lucro_liq_antes = linha[12]
            acoes_emitididas = linha[13]
            pay_jan = linha[14]
            pay_fev = linha[15]
            pay_mar = linha[16]
            pay_abr = linha[17]
            pay_mai = linha[18]
            pay_jun = linha[19]
            pay_jul = linha[20]
            pay_ago = linha[21]
            pay_set = linha[22]
            pay_out = linha[23]
            pay_nov = linha[24]
            pay_dez = linha[25]
            print("qtd meta: ", qtd_meta, "\nqtd atual: ", qtd_autal, "\npreco_atual: ", preco_atual, "\n")
            print("Preço Teto")
    print("\n\n\n")

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
        stock = input("Digite o ticket....: ")
        painel(stock.upper())



    if escolha == "99":
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






#INSERT INTO ticket (simbolo,empresa,tipo_acao,composicao,perc_payout_estatuto,dy_med_trien,preco_atual,qtd_meta,qtd_autal,vl_investido,
#previsao_receber,patri_liq_antes,lucro_liq_antes,acoes_emitididas,pay_jan,pay_fev,pay_mar,pay_abr,pay_mai,pay_jun,pay_jul,pay_ago,pay_set,pay_out,pay_nov,pay_dez)
#VALUES ('ITSA3','Itausa 3','PN',1,25,0.45,6.63,10000,100,863.00,'previsao_receber',65886000000,12200000000,9713183092,0,0,0,0,0,0,0,0,0,0,0,0)