enconder = {"A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            " ": "/"}

def morsee_encoder(text_input):
    text_encoded = ""
    
    for letter in text_input:
        text_encoded += enconder[letter] + " "

    print(text_encoded)

print("O QUE GOSTARIA DE FAZER?")
print("1 - ENCODER DE MORSE")

option = int(input("SELECIONE A OPÇÃO: "))

match option:
    case 1:
            text_input = input("Digite uma frase: ")
            text_input = text_input.upper()
            morsee_encoder(text_input)