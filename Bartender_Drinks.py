"""""
Complete the function that receives as input a string, and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	"Hipster Craft Beer"
"Bike Gang Member"	"Moonshine"
"Politician"	"Your tax dollars"
"Rapper"	"Cristal"
anything else	"Beer"
Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer".

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, the input "pOLitiCIaN" should still return "Your tax dollars".
"""

#PENDENTE APLICAR O ENCERRAMENTO

def menu():
    print("Digite \033[1mJabroni\033[0m para \033[1m\033[3mPatron Tequila\033[0m")
    print("Digite \033[1mSchool Counselor\033[0m para \033[1m\033[3mAnything with Alcohol\033[0m")
    print("Digite \033[1mProgrammer\033[0m para \033[1m\033[3mHipster Craft Beer\033[0m")
    print("Digite \033[1mBike Gang Member\033[0m para \033[1m\033[3mYour tax dollars\033[0m")
    print("Digite \033[1mRapper\033[0m para \033[1m\033[3mCristal\033[0m")
    print("Digite qualquer letra para \033[1mBeer🍻\033[0m")
    print("Texto normal e \033[1mtexto em negrito\033[0m.")
def selecao():
    opcao=str(input("Escolha uma das opções acima: "))
    opcao_ajustada=opcao.title()
    if opcao_ajustada=='Jabroni':
        print("\033[1m\033[3mPatron Tequila\033[0m")
    elif opcao_ajustada=='School Counselor':
        print("\033[1m\033[3mAnything with Alcohol\033[0m")
    elif opcao_ajustada=='Programmer':
        print("\033[1m\033[3mAnything with Alcohol\033[0m")    
    elif opcao_ajustada=='Bike Gang Member':
        print("\033[1m\033[3mHipster Craft Beer\033[0m")
    elif opcao_ajustada=='Rapper':
        print("\033[1m\033[3mCristal\033[0m")
    else:
        print("Beer🍻")
    main()    

def main():
    menu()
    selecao()
    
main()

""" Resolvendo de modo mais simples
def get_drink_by_profession(param):
    drinks = {"Jabroni": "Patron Tequila",
                "School Counselor": "Anything with Alcohol",
                "Programmer": "Hipster Craft Beer",
                "Bike Gang Member": "Moonshine",
                "Politician": "Your tax dollars",
                "Rapper": "Cristal"}
    return drinks[param.title()] if param.title() in drinks else "Beer"
"""
