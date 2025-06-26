print("Seja bem vindo ao App de vendas Jéssica Pedroso")
valor_do_pedido = float(input("Digite o valor do pedido: "))
quantidade_de_parcelas = float(input("Digite a quantidade de parcelas: "))
#condições if elif e else para validar a quantidade de parcelas
#para poder calcular o valor do juros sobre as parcelas
if quantidade_de_parcelas >= 4 and quantidade_de_parcelas <= 6:
#se o o valor da parcela for maior ou igual a 4 e menor ou igual a 6 vai calcular o juros de 4%
#e assim vai ser feito nas demais parcelas conforme a quantidade de parcelas que o cliente escolher
  juros = 0.04
  valor_da_parcela = valor_do_pedido * (1 + juros) / quantidade_de_parcelas
  valor_total_parcelado = valor_da_parcela * quantidade_de_parcelas
  print(f"Valor da parcela: {valor_da_parcela:.2f}")
  print(f"Valor total parcelado: {valor_total_parcelado:.2f}")
elif quantidade_de_parcelas >= 6 and quantidade_de_parcelas <= 9:
  juros = 0.08
elif quantidade_de_parcelas >= 9 and quantidade_de_parcelas <= 13:
  juros = 0.16
elif quantidade_de_parcelas >= 13:
  juros = 0.32
  valor_da_parcela = valor_do_pedido * (1 + juros) / quantidade_de_parcelas
  valor_total_parcelado = valor_da_parcela * quantidade_de_parcelas
  print(f"Valor da parcela: {valor_da_parcela:.2f}")
  print(f"Valor total parcelado: {valor_total_parcelado:.2f}")
elif quantidade_de_parcelas < 4:
#se for menor que 4 o juros deve ser 0%
  juros = 0.00
else:
#se não atender uma quantidade de parcelas validas vai retornar uma mensagem de erro
  print("Quantidade de parcelas inválida")




#Implementar o print com uma mensagem de boas-vindas e o menu.
print("Bem-vindo(a) ao sistema de pedidos da Marmitaria da Jéssica Pedroso!")
print("-" * 50) #Linha divisória para melhor visualização
print("Menu de Marmitas:")
print("Bife Acebolado (BA):")
print("  Tamanho P: R$ 16,00")
print("  Tamanho M: R$ 18,00")
print("  Tamanho G: R$ 22,00")
print("Filé de Frango (FF):")
print("  Tamanho P: R$ 15,00")
print("  Tamanho M: R$ 17,00")
print("  Tamanho G: R$ 21,00")
print("-" * 50)

total_pedido = 0.0 #Inicializa o acumulador de valor total do pedido

#Implementar as estruturas de while, break, continue
while True: #Loop principal para permitir múltiplos pedidos
    while True:#Loop para garantir um sabor válido
        sabor = input("Digite o sabor da marmita (BA para Bife Acebolado, FF para Filé de Frango): ").upper()
        if sabor in ['BA', 'FF']:
            break #Sai do loop de sabor se o input for válido
        else:
            print("Sabor inválido. Tente novamente.")#Mensagem de erro para sabor inválido
            continue#Volta ao início do loop de sabor para nova tentativa

    #Implementar o input do tamanho (P/M/G) e validação.
    while True:#Loop para garantir um tamanho válido
        tamanho = input("Digite o tamanho da marmita (P/M/G): ").upper()
        if tamanho in ['P', 'M', 'G']:
            break#Sai do loop de tamanho se o input for válido
        else:
            print("Tamanho inválido. Tente novamente.")#Mensagem de erro para tamanho inválido
            continue#Volta ao início do loop de tamanho para nova tentativa

    preco = 0.0#Inicializa o preço da marmita atual

    #Implementar if, elif e/ou else
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16.00
        elif tamanho == 'M':
            preco = 18.00
        else:
            preco = 22.00
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15.00
        elif tamanho == 'M':
            preco = 17.00
        else:
            preco = 21.00
    
    print(f"Você adicionou uma marmita de {sabor} tamanho {tamanho} no valor de R$ {preco:.2f}.")
    total_pedido += preco #Adiciona o preço da marmita atual ao acumulador

    #Pergunta para continuar ou encerrar.
    while True:#Loop para garantir uma resposta válida (sim/não)
        continuar = input("Deseja pedir mais alguma coisa? (sim/não): ").lower()
        if continuar in ['sim', 'não', 'nao']:
            break#Sai do loop de continuar se o input for válido
        else:
            print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            continue #Volta ao início do loop para nova tentativa
            
    if continuar == 'não' or continuar == 'nao':
        break #Sai do loop principal de pedidos se o usuário não quiser mais

print("-" * 50)
print(f"Total do seu pedido: R$ {total_pedido:.2f}") #Print do acumulador final
print("Obrigado por comprar conosco! Seu pedido está sendo preparado para retirada.")

print("Bem-vindo(a) ao sistema de pedidos! Desenvolvido por: Jessica Pedroso")  




# Função que pergunta o modelo da camiseta
def escolha_modelo():
    while True:
        print("\nModelos disponíveis:")
        print("MCS - Manga Curta Simples (R$ 1.80)")
        print("MLS - Manga Longa Simples (R$ 2.10)")
        print("MCE - Manga Curta com Estampa (R$ 2.90)")
        print("MLE - Manga Longa com Estampa (R$ 3.20)")
        modelo = input("Digite o código do modelo desejado: ").upper()

        if modelo == "MCS":
            return 1.80 
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido! Tente novamente.")  

# Função que pergunta a quantidade de camisetas
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Digite o número de camisetas: "))

            if quantidade > 20000:
                print("Quantidade excede o limite permitido. Tente novamente.") 
            elif quantidade < 20:
                return quantidade  # sem desconto
            elif quantidade < 200:
                return quantidade * 0.95  # 5% de desconto
            elif quantidade < 2000:
                return quantidade * 0.93  # 7% de desconto
            else:
                return quantidade * 0.88  # 12% de desconto
        except:
            print("Entrada inválida! Digite um número inteiro.")

# Função que pergunta o tipo de frete
def frete():
    while True:
        print("\nTipos de frete:")
        print("0 - Retirar na fábrica (R$ 0.00)")
        print("1 - Transportadora (R$ 100.00)")
        print("2 - Sedex (R$ 200.00)")
        tipo = input("Escolha o tipo de frete (0, 1 ou 2): ")

        if tipo == "0":
            return 0.00
        elif tipo == "1":
            return 100.00
        elif tipo == "2":
            return 200.00
        else:
            print("Opção de frete inválida. Tente novamente.")

# Código principal (main)
# Aqui chamamos as funções e calculamos o total a pagar

valor_modelo = escolha_modelo()
quantidade_com_desconto = num_camisetas()
valor_frete = frete()

# Calculando o valor total
total = (valor_modelo * quantidade_com_desconto) + valor_frete

# Exibindo o valor total com 2 casas decimais
print("\nResumo do pedido:")
print(f"Valor unitário da camiseta: R$ {valor_modelo:.2f}")
print(f"Quantidade com desconto aplicada: {quantidade_com_desconto:.2f}")
print(f"Frete: R$ {valor_frete:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
