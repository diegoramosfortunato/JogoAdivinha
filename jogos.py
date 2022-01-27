import random


print('*********************************')
print("Bem vindo ao  jodo de adivinhção!")
print('*********************************')

#declaração da variavel
numero_secreto = random.randrange(1,100)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldae : ")
print("(1)Fácil  (2)Médio  (3)Difícil ")

nivel = int(input("Defina o nível : "))

if(nivel == 1 ):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range(1 , total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada , total_de_tentativas) )
        #comando para o usuário digitar , e ser guardado na variavel
        chute = input("Digite um número entre 1 e 100 :  ")

        print("Você digitou : "  , chute )

        #declaração de variavel
        chute   =  int(chute)
        acertou =  chute ==  numero_secreto
        maior   =  chute >   numero_secreto
        menor   =  chute <   numero_secreto

        if(chute < 1 or chute > 100):
            print("Valor invalido, Digite um novo valor!")
            continue #vai continuar o codigo, diferente do break

        #estrutura condicional
        if(acertou):
            print("Você acertou  e fez {} pontos" .format(pontos))
            break
        else:
            if(maior ):
                 print("Você errou!! o seu chute foi maior que o número secreto")
            elif(menor):
                 print("Você errou!! o seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

print("Fim de jogo")