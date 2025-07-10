from dataclasses import dataclass
from enum import Enum,auto

class Usuario(Enum):
    aluno = auto()
    servidores_abaixo = auto()
    servidores_acima = auto()
    docente = auto()
    comunidade_externa = auto()

class forma_de_pag(Enum):
    Dinheiro = auto()
    PIX = auto()
    Cartao = auto()

@dataclass
class Venda():
    tipo : Usuario
    forma : forma_de_pag
    quantidade : int
    total_pagar : float
    
def main():
    ação = 0
    Vendas = [] #Lista que armazena as vendas
    while ação != 3:
        print("\n1-Cadastar uma venda\n2-Exibir o relatório \n3-Sair")
        ação = int(input("O que vc deseja executar? "))

        if ação == 1:
            print("\n 1-Aluno \n 2-Servidor abaixo de 3 salários \n 3-Servidor acima de 3 salários \n 4-Docente \n 5-Comunidade externa")
            Pessoa = int(input("Qual a relação do usuário com a UEM? "))
            
            if Pessoa == 1:
                Usu = Usuario.aluno
                quant = int(input("Quantos tickets você deseja? "))
                preço = 5.0
                pagar = preço * quant
                print("O valor a pagar é R$:", pagar ,)
                print("\n 1-Dinheiro \n 2-Cartão \n 3-PIX")
                Pagamento = int(input("Qual a forma de pagamento? "))

                if Pagamento == 1:
                    pag = forma_de_pag.Dinheiro                                       
                elif Pagamento == 2:
                    pag = forma_de_pag.Cartao                   
                elif Pagamento == 3:
                    pag = forma_de_pag.PIX
                
                Usuario1 = Venda(Usu, pag, quant ,pagar)
                Vendas.append(Usuario1)
                    

            elif Pessoa == 2:
                Usu = Usuario.servidores_abaixo
                quant = int(input("Quantos tickets você deseja? "))
                preço = 5.0
                pagar = preço * quant
                print("O valor a pagar é R$:", pagar ,)
                print("\n 1-Dinheiro \n 2-Cartão \n 3-PIX")
                Pagamento = int(input("Qual a forma de pagamento? "))
                if Pagamento == 1:
                    pag = forma_de_pag.Dinheiro                   
                elif Pagamento == 2:
                    pag = forma_de_pag.Cartao                 
                elif Pagamento == 3:
                    pag = forma_de_pag.PIX
                
                Usuario2 = Venda(Usu, pag, quant , pagar)
                Vendas.append(Usuario2)

            elif Pessoa == 3:
                Usu = Usuario.servidores_acima
                quant = int(input("Quantos tickets você deseja? "))
                preço = 10.0
                pagar = preço * quant
                print("O valor a pagar é R$:", pagar ,)
                print("\n 1-Dinheiro \n 2-Cartão \n 3-PIX")
                Pagamento = int(input("Qual a forma de pagamento? "))
                if Pagamento == 1:
                    pag = forma_de_pag.Dinheiro                    
                elif Pagamento == 2:
                    pag = forma_de_pag.Cartao                   
                elif Pagamento == 3:
                    pag = forma_de_pag.PIX
                
                Usuario3 = Venda(Usu , pag, quant , pagar)
                Vendas.append(Usuario3)
                    
            elif Pessoa == 4:
                Usu = Usuario.docente
                quant = int(input("Quantos tickets você deseja? "))
                preço = 10.0
                pagar = preço * quant
                print("O valor a pagar é R$:", pagar ,)
                print("\n 1-Dinheiro \n 2-Cartão \n 3-PIX")
                Pagamento = int(input("Qual a forma de pagamento? "))
                if Pagamento == 1:
                    pag = forma_de_pag.Dinheiro                   
                elif Pagamento == 2:
                    pag = forma_de_pag.Cartao                   
                elif Pagamento == 3:
                    pag = forma_de_pag.PIX

                Usuario4 = Venda(Usu, pag, quant ,pagar)
                Vendas.append(Usuario4)
                   
            elif Pessoa == 5:
                Usu = Usuario.comunidade_externa
                
                quant = int(input("Quantos tickets você deseja? "))
                preço = 19.0
                pagar = preço * quant
                print("O valor a pagar é R$:", pagar ,)
                print("\n 1-Dinheiro \n 2-Cartão \n 3-PIX")
                Pagamento = int(input("Qual a forma de pagamento? "))
                if Pagamento == 1:
                    pag = forma_de_pag.Dinheiro                  
                elif Pagamento == 2:
                    pag = forma_de_pag.Cartao                   
                elif Pagamento == 3:
                    pag = forma_de_pag.PIX
                
                Usuario5 = Venda(Usu, pag, quant ,pagar)
                Vendas.append(Usuario5)                    
        elif ação == 2:
            print("")
            print("")
            print("O total de tiquetes vendidos foi de: ", total_tiquetes(Vendas) ,)
            print("A receita do dia foi de R$: " , receita(Vendas) , )
            print("")
            print("")
            result = grafico_usuario(Vendas)
            print(result)
            print("")
            print("")
            result = grafico_pagamento(Vendas)
            print(result)
                       
def total_tiquetes(Vendas) -> int: 
    """
    Exemplos:
    >>> Vendas = [Venda(Usuario.aluno, forma_de_pag.Dinheiro, 1, 5.0), Venda(Usuario.aluno, forma_de_pag.Cartao, 10, 50.0), Venda(Usuario.servidores_acima, forma_de_pag.PIX, 3, 30.0)]   
    >>> total_tiquetes(Vendas)
    14
    """
    total = 0
    for item in Vendas:
            total += item.quantidade
    return total

def receita(Vendas) -> float:
    """
    Exemplos:
    >>> Vendas = [Venda(Usuario.aluno, forma_de_pag.Dinheiro, 1, 5.0), Venda(Usuario.aluno, forma_de_pag.Cartao, 10, 50.0), Venda(Usuario.servidores_acima, forma_de_pag.PIX, 3, 30.0)]   
    >>> receita(Vendas)
    85.0
    """
    receita_dia = 0.0
    for item in Vendas:
        receita_dia += item.total_pagar  
    return receita_dia

def porcentagem_receita(Vendas: list, forma_de_pagamento: forma_de_pag) -> int:
    """
    Exemplos:
    >>> Vendas = [Venda(Usuario.aluno, forma_de_pag.Dinheiro, 1, 5.0), Venda(Usuario.aluno, forma_de_pag.Cartao, 10, 50.0), Venda(Usuario.servidores_acima, forma_de_pag.PIX, 3, 30.0)]   
    >>> porcentagem_receita(Vendas, forma_de_pag.Cartao)
    59
    >>> porcentagem_receita(Vendas, forma_de_pag.Dinheiro)
    6
    >>> porcentagem_receita(Vendas, forma_de_pag.PIX)
    35

    """
    receita_total = receita(Vendas)
    receita_forma = 0.0
    for item in Vendas:
        if item.forma == forma_de_pagamento:
            receita_forma += item.total_pagar
        porcentagem_rec = round((receita_forma / receita_total) * 100)
    return porcentagem_rec

def porcentagem_tiquetes(Vendas: list, tipo_usuario: Usuario) -> int:
    """
    Exemplos:
    >>> Vendas = [Venda(Usuario.aluno, forma_de_pag.Dinheiro, 1, 5.0), Venda(Usuario.aluno, forma_de_pag.Cartao, 10, 50.0), Venda(Usuario.servidores_acima, forma_de_pag.PIX, 3, 30.0)]   
    >>> porcentagem_tiquetes(Vendas , Usuario.aluno)
    79
    >>> porcentagem_tiquetes(Vendas , Usuario.servidores_abaixo)
    0
    >>> porcentagem_tiquetes(Vendas , Usuario.servidores_acima)
    21
    >>> porcentagem_tiquetes(Vendas , Usuario.docente)
    0
    >>> porcentagem_tiquetes(Vendas , Usuario.comunidade_externa)
    0
    """
    total_tiquets = total_tiquetes(Vendas)  
    total_tipo = 0
    for item in Vendas:
        if item.tipo == tipo_usuario:
            total_tipo += item.quantidade  
        porcentagem_tiq = round((total_tipo / total_tiquets) * 100)
    return porcentagem_tiq

def grafico_usuario(Vendas):
    """ 
    Exemplos:
    >>>  Vendas = [Venda(Usuario.aluno, forma_de_pag.Dinheiro, 1, 5.0), Venda(Usuario.aluno, forma_de_pag.Cartao, 10, 50.0), Venda(Usuario.servidores_acima, forma_de_pag.PIX, 3, 30.0)]
    >>> grafico_usuario(Vendas)
    "Aluno: [==============================================================================] (79%)
    Servidores Abaixo: [] (0%)
    Servidores Acima: [=====================] (21%)
    Docente: [] (0%)
    Comunidade Externa: [] (0%)"
    """
     
    porcentagem_aluno = porcentagem_tiquetes(Vendas, Usuario.aluno)
    porcentagem_servidores_abaixo = porcentagem_tiquetes(Vendas, Usuario.servidores_abaixo)
    porcentagem_servidores_acima = porcentagem_tiquetes(Vendas, Usuario.servidores_acima)
    porcentagem_docente = porcentagem_tiquetes(Vendas, Usuario.docente)
    porcentagem_comunidade_externa = porcentagem_tiquetes(Vendas, Usuario.comunidade_externa)

    grafico_aluno = f"Aluno: [{'=' * int(porcentagem_aluno)}] ({int(porcentagem_aluno)}%)\n"
    grafico_servidores_abaixo = f"Servidores Abaixo: [{'=' * int(porcentagem_servidores_abaixo)}] ({int(porcentagem_servidores_abaixo)}%)\n"
    grafico_servidores_acima = f"Servidores Acima: [{'=' * int(porcentagem_servidores_acima)}] ({int(porcentagem_servidores_acima)}%)\n"
    grafico_docente = f"Docente: [{'=' * int(porcentagem_docente)}] ({int(porcentagem_docente)}%)\n"
    grafico_comunidade_externa = f"Comunidade Externa: [{'=' * int(porcentagem_comunidade_externa)}] ({int(porcentagem_comunidade_externa)}%)\n"

    return grafico_aluno + grafico_servidores_abaixo + grafico_servidores_acima + grafico_docente + grafico_comunidade_externa

def grafico_pagamento(Vendas):
    """
    Exemplos:
    >>> Vendas = [Venda(Usuario.aluno, forma_de_pag.Dinheiro, 1, 5.0), Venda(Usuario.aluno, forma_de_pag.Cartao, 10, 50.0), Venda(Usuario.servidores_acima, forma_de_pag.PIX, 3, 30.0)]
    >>> grafico_pagamento(Vendas)
    "Dinheiro: [=================================] (33%)
    Cartao: [=================================] (33%)
    PIX: [=================================] (33%)"
    """
    porcentagem_Dinheiro = porcentagem_receita(Vendas, forma_de_pag.Dinheiro)
    porcentagem_Cartao = porcentagem_receita(Vendas, forma_de_pag.Cartao)
    porcentagem_PIX = porcentagem_receita(Vendas, forma_de_pag.PIX)
    

    grafico_dinheiro = (f"Dinheiro: [{'=' * int(porcentagem_Dinheiro)}] ({int(porcentagem_Dinheiro)}%)\n")
    grafico_cartao = (f"Cartão: [{'=' * int(porcentagem_Cartao)}] ({int(porcentagem_Cartao)}%)\n")
    grafico_PIX = f"PIX: [{'=' * int(porcentagem_PIX)}] ({int(porcentagem_PIX)}%)\n"

    return grafico_dinheiro + grafico_cartao + grafico_PIX

if __name__ == "__main__":
    main()
