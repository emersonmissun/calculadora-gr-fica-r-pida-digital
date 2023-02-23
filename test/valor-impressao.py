#! /bin/env python3

# Preço de impressão colorida e preto e branco

# Autor: Emerson Missun
# Data: 2020-10-29
# Atualização: 2020-10-29
# Versão: 0.1

# Linguagem de programação: Python 3.8.5
# Bibliotecas e módulos: pandas, locale 
# Testado e homologado nos sistemas operacionais: 
	# Linux Ubuntu 20.04.1 LTS
# Link do repositório: 
    # https://github.com/EmersonMissun/valor-impressao

# Suporte: Nerds na Cadeira Tecnologia e Informática
	# Site: https://nerdsnacadeira.com.br
	# E-mail: nerdsnacadeira@gmail.com
	# Telefone: (61) 9 8459-0135
# Licença: GNU General Public License v3.0
 

# Descrição: Script para carregar os valores de impressão colorida e preto e branco de uma planilha e retornar os valores para o script principal do programa. 
# O arquivo excel deve estar na pasta data/Dados_Entrada/expenses/impressao_custos.xlsx.
# O arquivo excel deve conter duas abas, uma para impressão colorida e outra para impressão preto e branco.
# A aba de impressão colorida deve conter as colunas: tipo, PRINT_A4, PRINT_A3, PRINT_A2, PRINT_A1, PRINT_A0, PRINT_A0+ e demais formatos comercializados e os valores de impressão para cada tipo de impressão (ex.: IMG_COR, TXT_COR, TXT_IMG_COR). 
# A aba de impressão preto e branco deve conter as colunas: tipo_pb, PRINT_A4_PB, PRINT_A3_PB, PRINT_A2_PB, PRINT_A1_PB, PRINT_A0_PB, PRINT_A0+_PB e demais formatos comercializados e os valores de impressão para cada tipo de impressão (ex.: IMG_PB, TXT_PB, TXT_IMG_PB). 


# Importar bibliotecas e módulos necessários para o script funcionar corretamente 
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Carregar o arquivo de dados em excel com valor e tipos de impressão
valor_cor = pd.read_excel('data/Dados_Entrada/expenses/impressao_custos.xlsx', sheet_name='cor', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), nrows=3)
valor_pb = pd.read_excel('data/Dados_Entrada/expenses/impressao_custos.xlsx', sheet_name='pb', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), nrows=3)

# print(valor_cor)	# Exibe os valores de impressão colorida na tela do terminal 
# print(valor_pb)	# Exibe os valores de impressão preto e branco na tela do terminal

## Valores de impressão cor
valor_img_cor = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A4'].item() # NOTE: o item() retorna o valor do item da coluna especificada 
valor_img_cor = locale.currency(valor_img_cor, grouping=True)

valor_txt_cor = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A4'].item()
valor_txt_cor = locale.currency(valor_txt_cor, grouping=True)

valor_txt_img_cor = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A4'].item()
valor_txt_img_cor = locale.currency(valor_txt_img_cor, grouping=True)

## Valores de impressão PB
valor_img_pb = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A4_PB'].item()
valor_img_pb = locale.currency(valor_img_pb, grouping=True)

valor_txt_pb = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A4_PB'].item()
valor_txt_pb = locale.currency(valor_txt_pb, grouping=True)

valor_txt_img_pb = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A4_PB'].item()
valor_txt_img_pb = locale.currency(valor_txt_img_pb, grouping=True)

print("")
print("-------------------------------------------------------------------")
print("Valores de impressão colorida e preto e branco")
print("Print Textos PB =", valor_txt_pb) # 0.01
print("Print Textos e Imagens PB =", valor_txt_img_pb) # 0.01
print("Print Foto PB =", valor_img_pb) # 0.01

print("")
print("Valores de impressão colorida e preto e branco")
print("Print Textos Cor =", valor_txt_cor) # 0.01
print("Print Textos e Imagens Cor =", valor_txt_img_cor) # 0.01
print('Print Foto Cor =', valor_img_cor) # 0.01
print("-------------------------------------------------------------------")
print("")

# Exemplo de saída do script:
# Print Textos PB = R$ 0,01
# Print Textos e Imagens PB = R$ 0,01
# Print Foto PB = R$ 0,01

# Print Textos Cor = R$ 0,01
# Print Textos e Imagens Cor = R$ 0,01
# Print Foto Cor = R$ 0,01

# Fim do script

print("")
