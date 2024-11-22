""""
https://github.com/hevalhazalkurt/codewars_python_solutions/blob/master/8kyuKatas/Sum_Arrays.md
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. 
If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.
"""

def obter_numeros():
   
    numeros = []  # Lista para armazenar os números
    while True:
        entrada = input("Digite um número para adicionar à lista (ou 'fim' para parar): ")
        if entrada.lower() == 'fim':  # Se o usuário digitar 'fim', o loop é interrompido
            break
        try:
            # Tenta converter a entrada para um número (inteiro ou flutuante)
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")  # Mensagem de erro se a entrada não for um número
    return numeros
    

def soma_lista(lista_numeros): 
    print("Os números inseridos são:", lista_numeros)
    soma = 0
    for numero in lista_numeros:
        soma = soma+numero

    return soma

def main():
    # Chama a função e exibe a lista de números
    lista_numeros = obter_numeros()
    total=soma_lista(lista_numeros)
    print(f"O valor da soma é: {total}")

if __name__ == '__main__':
    main()
