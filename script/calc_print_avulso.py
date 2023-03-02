#! /bin/env python

# Calculadora de Print Avulso
# Este script calcula o valor de impressão de um arquivo em PDF

# Importando as variáveis dos arquivos externos
from ..data.Dados_Entrada.expenses.papeis_var import valor_mbase
from ..data.Dados_Entrada.expenses.valor_impressao import valor_cor, valor_pb

# Pedindo as informações do usuário
tipo_impressao = int(input("Digite 1 para impressão preto e branco, 2 para colorida ou 3 para mista: "))
if tipo_impressao == 3:
    paginas_pb = int(input("Digite a quantidade de páginas: "))
    paginas_cor = int(input("Digite a quantidade de colorida: "))
else:
    paginas = int(input("Digite a quantidade de páginas: "))
    duplex = input("Será frente e verso (S/N)? ").upper() == "S"

# Calculando o preço
if tipo_impressao == 1:
    preco_unitario = valor_cor["PB"]
elif tipo_impressao == 2:
    preco_unitario = valor_pb["COLOR"]
else:
    preco_unitario = paginas_pb * valor_pb["PB"] + paginas_cor * valor_cor["COLOR"]
if duplex:
    preco_unitario *= 2
preco_total = preco_unitario * paginas // 2

# Imprimindo o resultado
print(f"O preço total é: R$ {preco_total:.2f}")
