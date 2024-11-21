def inicio():
    mostrarlinha()
    print ("💥SEJA BEM VINDO AO VALIDADOR PAR OU ÍMPAR💥")
    mostrarlinha()

def menu():
    mostrarlinha()
    print ("1. Começar")
    print ("2. Sair")

def encerramento():
    
    os.system('cls')
    mostrarlinha()
    print("Encerrando o Programa")
    mostrarlinha()

def opcao_invalida():
     print('Opção Inválida\n')
     input('Digite uma tecla para retornar a tela principal ') 
     main()

def selecionando():
   # try:
    opcao=int(input("Escolha uma das opções acima: "))
    if opcao==1:
        recebe_numero()
    elif opcao==2:
        encerramento()
    else:
        opcao_invalida()
    #except Exception as e:
     #print(str(e))

def validador(entrada):
    resto = entrada%2
    if resto==0:
        print(f'O número {entrada} é PAR')
    else:
        print(f'O número {entrada} é ÍMPAR')

def recebe_numero():
    mostrarlinha()
    print("Chegou a hora, vamos começar!!!")
    mostrarlinha()
    entrada=float(input("Insira o número que deseja validar: "))
    validador(entrada)

def main():
    inicio()
    menu()
    selecionando()

if __name__ == '__main__':
    main()
