# Se o sistema estiver em ambiente de produção# Se o sistema estiver em ambiente de produção
# Mude a variável para True
prod = False

if prod == False:
    garagem = [
        {
            "modelo": "Uno",
            "cor": "Branco",
            "km": "0",
            "ano": "2016",
            "marca": "Fiat",
            "placa": "ABC1234"
        },
        {
            "modelo": "Peugeot 206",
            "cor": "Preto",
            "km": "80000",
            "ano": "2015",
            "marca": "Peugeot",
            "placa": "ADD1549"
        },
        {
            "modelo": "Polo",
            "cor": "Branco",
            "km": "60000",
            "ano": "2025",
            "marca": "Volkswagen",
            "placa": "QCY7894"
        },
        {
            "modelo": "FZ25",
            "cor": "Vermelha",
            "km": "25000",
            "ano": "2025",
            "marca": "Yamaha",
            "placa": "TCU4578"
        }
    ]

else:
    garagem = [] # Criando lista para guardar os veiculos

while True:
    print("-" * 30)
    # Apresentando menu para o usuário
    print(" -- Bem-vindo a concessionária! --")
    print("1 - Cadastro de veiculo")
    print("2 - Atualização de veiculo")
    print("3 - Remoção de veiculo")
    print("4 - Listagem de veiculo")
    print("5 - Sair")

    # Pedido ao usuário uma opção
    escolha = input("Escolha uma opção: ")

    # Convertendo a resposta do usuário em INTEIRO e comprando com o numero 1
    if int(escolha) == 1:
        print("-" * 30)
        print("Cadastrando veiculo...") # Apresentando ao usuário o sistema de cadastro

        # Guardando os valores de cada dado em determinada variavel
        # (modelo, cor, km, ano, marca e placa)
        modelo = input("Qual modelo do veiculo? ")
        cor = input("Qual a cor do veiculo? ")
        km = input("Quantos km o veiculo já andou? ")
        ano = input("Qual o ano do veiculo? ")

        # Verificando km e ano se são menor que zero
        # Caso for verdadeiro, o código é interrompido
        if int(km) < 0 or int(ano) < 0:
            print("Valor invalida (menor que zero)")
            exit()

        # Verificando se a variavel ano é menor ou igual a 2015
        # Caso for verdadeiro, o código é interrompido
        if int(ano) <= 2015:
            print("Carro fora do ano limite de aceitação.")
            exit()

        # Pedindo o restante das informações
        marca = input("Qual a fabricante do veiculo? ")
        placa = input("Qual a placa de identificação do veiculo? ")

        # Verificando se as strings estão vazias, removendo os espaços do inicio e do fim
        # srip() elimina os espaços
        if modelo.strip() == "" or cor.strip() == "" or marca.strip() == "" or placa.strip() == "":
            print("valor invalido (não pode ser vazio)")
            exit()

        # Guardando as informações em um dicionário
        veiculo = {
            "modelo": modelo,
            "cor": cor,
            "km": km,
            "ano": ano,
            "marca": marca,
            "placa": placa
        }

        # Adicionando o veiculo a lista da garagem
        garagem.append(veiculo)

        # Voltando uma resposta pro usuário com uma mensagem de sucesso!
        print(f"Veiculo {veiculo['modelo']} adicionado com sucesso!")

    elif int(escolha) == 2:
        print("=" * 10)
        print("Alterando dados do veiculo...")
        # Pedindo a placa do veiculo para atualizar
        placa = input("Digite a placa do veiculo: ")
        # Para cada veiculo na garagem
        for veiculo in garagem:
            # Verifica se a placa do veiculo é a mesma digitada pelo usuario
            if veiculo["placa"] == placa:
                # Salva o indice(inteiro) di=o veiculo na garagem
                index = garagem.index(veiculo)
                # Pega a chave e o valor de cada item do veiculo
                for chave, valor in veiculo.items():
                    print("-" * 10)
                    # Pedir um novo valor para determinado dado(cor, modelo, marca, etc...)
                    novo_valor = input(f"Escolha um novo valor para {chave} (valor atual: {valor}): ")
                    # Se o novo_valor dor vazio, não faz nada(deixa como estava)
                    # Se o novo_valor não for vazio(!=)
                    if novo_valor.strip() != "":
                        # Atualiza o valor do veiculo utilizando o indice da garagem
                        garagem[index][chave] = novo_valor
                break

        else:
            print("Veiculo não encontrado.")

    elif int(escolha) == 3:
        print("=" * 10) # Imprimindo uma linha para separação
        print("Removendo veiculo...") # Imprimindo mensagem para o usuario

        # Pedindo ao usuario a placa do veiculo para remover
        placa = input("Digite a placa do veiculo: ")

        # Para cada viculo(dicionário) na garagem(lista)
        for veiculo in garagem:
            # Verifica se a placa do veiculo(ja cadastrado) é identifica a placa que o usuario digitou
            if veiculo["placa"] == placa:
                # Remove o veiculo da lista
                garagem.remove(veiculo)
                # Imprimi uma mensagem de sucesso
                print("Veiculo removido com sucesso!")
                # Inerrompe a repetição(for)
                break
        # Executa o else APENAS se o laço de repetição(for)
        else:
            print("Veiculo não encontrado!")

    elif int(escolha) == 4:
        print("-" * 30)
        print("Listando veiculos")

        # Vrifica se a garagem está vazia
        # Se estiver vazia, imprime uma mensagem na tela
        if not garagem:
            print("Nenhum veiculo cadastrado")

        # Se a lista conter items(veiculos)
        else:
            # Para cada veiculo na lista(garagem)
            # Imprime uma mensagem amigavel contendo as informações do veiculo
            for veiculo in garagem:
                print("-" * 30)
                print(f"Modelo: {veiculo["modelo"]}")
                print(f"Cor: {veiculo["cor"]}")
                print(f"Fabricante: {veiculo["marca"]}")
                print("-" * 30)

    elif int(escolha) == 5:
        print("Volte sempre!")
        break

    else:
        print("Opção invalida")