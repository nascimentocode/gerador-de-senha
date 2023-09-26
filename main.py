from random import choice
import string

def generatePassword(char, passwordLength):
    password = ''
    for i in range(passwordLength):
        password += choice(char)
    
    return password

def transformListIntoString(list):
    char = ''
    for c in list:
        char += c
    
    return char


def main():
    listChar = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

    print("==================== GERADOR DE SENHA ====================\n")
    
    questions = ["Você quer que sua senha contenha caracteres minusculos? S/N\n", 
                    "Você quer que sua senha contenha caracteres maiusculos? S/N\n", 
                    "Você quer que sua senha contenha números? S/N\n",
                    "Você quer que sua senha contenha caracter especial? S/N\n"]

    for i in range(4):
        result = input(questions[i])

        if result.upper() == 'N':
            listChar.pop(i)

    passwordLength = int(input("Quantos dígitos sua senha deve ter?"))

    char = transformListIntoString(listChar)

    print(f"Sua senha criada é: {generatePassword(char, passwordLength)}")

main()