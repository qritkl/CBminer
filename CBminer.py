from random import choice
from string import ascii_lowercase,digits
from os import system,listdir
from threading import Thread as t

CHARS = ascii_lowercase+digits
print("o que fazer?")
print("[A]---finitas vezes | [B]---infinitas :")
opcao = input("--> ").upper()

if opcao != "A" and opcao != "B":
    print("resposta inválida!!!script encerrado")
    exit()

elif opcao=="A":
    TRIES = int(input("tentar quantas dúzias de vezes?: "))

print("procurar por extensões:")
print("1---png|2---jpg|3---svg|4---webp")
print("5---mp4|6---mp3|7---pdf|8---outros")
try:
    extensao = int(input("--> "))
except ValueError:
    print("valor errado, o script será encerrado")
    exit()
else:
    pass



formato=str()

match extensao:
    case 1:
        formato="png"
    case 2:
        formato="jpg"
    case 3:
        formato="svg"
    case 4:
        formato="webp"
    case 5:
        formato="mp4"
    case 6:
        formato="mp3"
    case 7:
        formato="pdf"
    case 8:
        formato = input("qual o formato(sem o \".\")? ")
        if "." in formato:
            print("todos os pontos adicionados serao removidos!!!")
            formato.replace(".","")
    case _:
        exit()

def tentativa():
    global formato
    random_string = ""
    for x in range(6):
        random_string += choice(CHARS)
    
    system(f"wget https://files.catbox.moe/{random_string}.{formato} &> /dev/null")

# vou pesquisar como fazer de outra forma
def multiTeste():
    t1 = t(target=tentativa)
    t2 = t(target=tentativa)
    t3 = t(target=tentativa)
    t4 = t(target=tentativa)
    t5 = t(target=tentativa)
    t6 = t(target=tentativa)
    t7 = t(target=tentativa)
    t8 = t(target=tentativa)
    t9 = t(target=tentativa)
    t10 = t(target=tentativa)
    t11 = t(target=tentativa)
    t12 = t(target=tentativa)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()

if __name__=="__main__":
    arquivos_antes = listdir()
    if opcao == "A":
        for x in range(TRIES):
            print(f"{x+1}/{TRIES} DE TENTATIVAS EFETUADAS!!!aguarde.")
            multiTeste()
            print(f"{len(listdir())-len(arquivos_antes)} arquivos encontrados!")
    elif opcao == "B":
        while True:
            multiTeste()
            print(f"{len(listdir())-len(arquivos_antes)} arquivos encontrados!")