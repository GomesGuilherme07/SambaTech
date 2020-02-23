import random
from time import  sleep
import null as null

#Função Anagrama
def anagrama():
    print('ANAGRAMA - Digite duas palavras para serem verificadas')
    a = str(input('Favor digitar uma palavra: ')).upper().strip()
    b = str(input('Favor digitar outra palavra: ')).upper().strip()

    aInventido = a[::-1]

    if (b == aInventido):
        print(f'A palavra {a} é um anagrama da palavra {b}')
        print('Retornando ao menu...')
        sleep(2)
    else:
        print(f'A palavra {a} não é um anagrama da palavra {b}')
        print('Retornando ao menu...')
        sleep(2)

#Função Ordenando Vetor
def ordenando():
    print('ORDENANDO VETOR')
    vetor = []
    vetorpar = []
    vetorimpar = []
    aux = 0

    print('Gerando Vetor Aleatório com números inteiros de 1 a 100: ')

    for i in range(1, 7):
        vetor.insert(0, random.randint(1, 100))

    print(vetor)

    print('Ordenando vetor ')

    for i in range(0, 6):
        if (vetor[i] % 2) == 0:
            vetorpar.append(vetor[i])  # Inserindo valores pares em um vetor separado
        else:
            vetorimpar.append(vetor[i])  # Inserindo valores impares em um vetor separado

    tVetorPar = len(vetorpar)
    tVetorImpar = len(vetorimpar)

    vetorpar = sorted(vetorpar, reverse=True)  # Ordenação ordem decrescente
    vetorimpar = sorted(vetorimpar)  # ordenação ordem crescente

    vetor.clear()

    vetor = vetorpar + vetorimpar

    print(vetor)

    print('Retornando ao menu...')
    sleep(2)

#Função Decompondo Valor
def decompondo():
    print('DECOMPOSIÇÃO DE VALOR')
    valor = float(input('Digite um valor: '))

    print(f'Decomposição do valor R${valor}')

    nota100 = valor // 100
    print(f'{nota100} nota de R$100,00')
    valor = valor % 100

    nota50 = valor // 50
    print(f'{nota50} nota de R$50,00')
    valor = valor % 50

    nota20 = valor // 20
    print(f'{nota20} nota de R$20,00')
    valor = valor % 20

    nota10 = valor // 10
    print(f'{nota10} nota de R$10,00')
    valor = valor % 10

    nota5 = valor // 5
    print(f'{nota5} nota de R$5,00')
    valor = valor % 5

    nota2 = valor // 2
    print(f'{nota2} nota de R$2,00')
    valor = valor % 2

    moeda1 = valor // 1
    print(f'{moeda1} moeda de R$1,00')
    valor = valor % 1

    moeda50 = valor // 0.5
    print(f'{moeda50} moeda de R$0.5')
    valor = valor % 0.5

    moeda10 = valor // 0.1
    print(f'{moeda10} moeda de R$0,10')
    valor = valor % 0.1

    moeda05 = valor // 0.05
    print(f'{moeda05} moeda de R$0,05')
    valor = valor % 0.05

    moeda01 = valor // 0.01
    print(f'{moeda01} moeda de R$0,1')
    valor = valor % 0.01

    print('Retornando ao menu...')
    sleep(3)

#Função Gerenciamento de mídia
def midia():
    id = 0
    nome = ''
    url = ''
    duracao = 0
    idMidias = []
    nomeMidias = []
    urlMidias = []
    duracaoMidias = []

    print('CRIAR MÍDIA')

    qtdeMidias = int(input('Digite a quantidade de mídias a serem armazenadas: '))
    for i in range(0, qtdeMidias):
        print(f'----- {i + 1}ª mídia -----')
        id += 1
        idMidias.append(id)

        # Condição para garantir a entrada de dados na varivael nome
        aux = 0
        while aux != 1:
            nome = str(input('Digite o nome da mídia: '))
            if nome != null:
                nomeMidias.append(nome)
                aux = 1
            else:
                print('Não foi informado nenhum nome. Tente novamente.')

            url = str(input('Digite a URL da mídia: '))
            urlMidias.append(url)

            duracao = int(input('Digite a duração da mídia: '))
            duracaoMidias.append(duracao)

    print('LISTAR MÍDIA')
    tamanho = len(idMidias)
    for i in range(0, tamanho):
        print(f'ID: {idMidias[i]} -- Nome: {nomeMidias[i]} -- URL: {urlMidias[i]} -- Duração: {duracaoMidias[i]}')
    sleep(2)

    print('BUSCAR MÍDIA')
    buscaId = int(input('Digite o ID de uma mídia: '))
    tamanho = len(idMidias)
    verifica = False

    for i in range(0, tamanho):
        if idMidias[i] == buscaId:
            verifica = True

    if verifica == True:
        print(f'ID: {idMidias[i]} -- Nome: {nomeMidias[i]} -- URL: {urlMidias[i]} -- Duração: {duracaoMidias[i]}')
    else:
        print(f'Mídia de ID {buscaId} não escontrada.')

    print('Retornando ao menu...')
    sleep(2)

#Menu pricipal do programa
opcao = 0
while opcao != 5:
    print('========== GUILHERME DE OLIVEIRA GOMES ===========')
    print('========== DESAFIO TÉCNICO - SAMBA TECH ==========')

    print("""
    [1] Anagrama
    [2] Ordenando vetor
    [3] Decompondo valor
    [4] Gerenciamento de mídias
    [5] Sair do programa""")
    opcao = int(input('\nEscolha uma opção de 1 a 5: '))

    if opcao == 1:
        anagrama()

    elif opcao == 2:
        ordenando()

    elif opcao == 3:
        decompondo()

    elif opcao == 4:
        midia()

    elif opcao == 5:
        print('Fim do programa, Obrigado !!!')
        sleep(2)

    else:
        print('Opção inválida. Tente Novamente ...')
        sleep(2)









