#! /bin/env python 

# Carregar o arquivo de dados em excel com valores de papeis variáveis por tipos e tamanhos
# O arquivo deve estar na pasta data/Dados_Entrada/expenses e deve ter o nome materiais.xlsx
import pandas as pd # para ler o arquivo excel
import locale # para formatar os valores
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # para formatar os valores
import os # para pegar o caminho do arquivo
import sys # para pegar o caminho do arquivo

## Carregar arquivo de dados
valor_mbase = pd.read_excel('data/Dados_Entrada/expenses/Materiais.xlsx', sheet_name='MBASE', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8), nrows=4)

print(valor_mbase) # para testar se o arquivo foi carregado corretamente

# Definir os valores de cada papel Sulfite 75g Branco
valor_sulfite75A3 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A3'].item() 
valor_sulfite75A3 = locale.currency(valor_sulfite75A3, grouping=True)

valor_sulfite75A4 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A4'].item() 
valor_sulfite75A4 = locale.currency(valor_sulfite75A4, grouping=True)

valor_sulfite75A5 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A5'].item()
valor_sulfite75A5 = locale.currency(valor_sulfite75A5, grouping=True)

valor_sulfite75A6 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A6'].item()
valor_sulfite75A6 = locale.currency(valor_sulfite75A6, grouping=True)

valor_sulfite75A7 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A7'].item()
valor_sulfite75A7 = locale.currency(valor_sulfite75A7, grouping=True)

valor_sulfite75A8 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A8'].item()
valor_sulfite75A8 = locale.currency(valor_sulfite75A8, grouping=True)

valor_sulfite75A9 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A9'].item()
valor_sulfite75A9 = locale.currency(valor_sulfite75A9, grouping=True)

valor_sulfite75A10 = valor_mbase.loc[valor_mbase['MBASE'] == 'Sulfite 75g Branco', 'PRECO_MIDIA_A10'].item()
valor_sulfite75A10 = locale.currency(valor_sulfite75A10, grouping=True) # para formatar os valores em moeda

# Definir os valores de cada papel Glossy 180g Branco
valor_glossy130A3 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A3'].item() 
valor_glossy130A3 = locale.currency(valor_glossy130A3, grouping=True)

valor_glossy130A4 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A4'].item()
valor_glossy130A4 = locale.currency(valor_glossy130A4, grouping=True)

valor_glossy130A5 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A5'].item()
valor_glossy130A5 = locale.currency(valor_glossy130A5, grouping=True)

valor_glossy130A6 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A6'].item()
valor_glossy130A6 = locale.currency(valor_glossy130A6, grouping=True)

valor_glossy130A7 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A7'].item()
valor_glossy130A7 = locale.currency(valor_glossy130A7, grouping=True)

valor_glossy130A8 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A8'].item()
valor_glossy130A8 = locale.currency(valor_glossy130A8, grouping=True)

valor_glossy130A9 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A9'].item()
valor_glossy130A9 = locale.currency(valor_glossy130A9, grouping=True)

valor_glossy130A10 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 180g', 'PRECO_MIDIA_A10'].item()
valor_glossy130A10 = locale.currency(valor_glossy130A10, grouping=True) # para formatar os valores em moeda

# Definir os valores de cada papel Glossy 230g
valor_glossy230A3 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A3'].item() 
valor_glossy230A3 = locale.currency(valor_glossy230A3, grouping=True)

valor_glossy230A4 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A4'].item()
valor_glossy230A4 = locale.currency(valor_glossy230A4, grouping=True)

valor_glossy230A5 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A5'].item()
valor_glossy230A5 = locale.currency(valor_glossy230A5, grouping=True)

valor_glossy230A6 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A6'].item()
valor_glossy230A6 = locale.currency(valor_glossy230A6, grouping=True)

valor_glossy230A7 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A7'].item()
valor_glossy230A7 = locale.currency(valor_glossy230A7, grouping=True)

valor_glossy230A8 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A8'].item()
valor_glossy230A8 = locale.currency(valor_glossy230A8, grouping=True)

valor_glossy230A9 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A9'].item()
valor_glossy230A9 = locale.currency(valor_glossy230A9, grouping=True)

valor_glossy230A10 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Glossy 230g', 'PRECO_MIDIA_A10'].item()
valor_glossy230A10 = locale.currency(valor_glossy230A10, grouping=True) # para formatar os valores em moeda

# Definir os valores de cada papel Fotográfico Matte 108g
valor_matte108A3 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A3'].item() 
valor_matte108A3 = locale.currency(valor_matte108A3, grouping=True)

valor_matte108A4 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A4'].item()
valor_matte108A4 = locale.currency(valor_matte108A4, grouping=True)

valor_matte108A5 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A5'].item()
valor_matte108A5 = locale.currency(valor_matte108A5, grouping=True)

valor_matte108A6 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A6'].item()
valor_matte108A6 = locale.currency(valor_matte108A6, grouping=True)

valor_matte108A7 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A7'].item()
valor_matte108A7 = locale.currency(valor_matte108A7, grouping=True)

valor_matte108A8 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A8'].item()
valor_matte108A8 = locale.currency(valor_matte108A8, grouping=True)

valor_matte108A9 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A9'].item()
valor_matte108A9 = locale.currency(valor_matte108A9, grouping=True)

valor_matte108A10 = valor_mbase.loc[valor_mbase['MBASE'] == 'Fotográfico Matte 108g', 'PRECO_MIDIA_A10'].item()
valor_matte108A10 = locale.currency(valor_matte108A10, grouping=True)

# print(" ")
# print('Papel Sulfite 75g', '----------------------------------')
# print('Papel Sulfite 75g Branco A3 = ', valor_sulfite75A3)
# print('Papel Sulfite 75g Branco A4 = ', valor_sulfite75A4)
# print('Papel Sulfite 75g Branco A5 = ', valor_sulfite75A5)
# print('Papel Sulfite 75g Branco A6 = ', valor_sulfite75A6)
# print('Papel Sulfite 75g Branco A7 = ', valor_sulfite75A7)
# print('Papel Sulfite 75g Branco A8 = ', valor_sulfite75A8)
# print('Papel Sulfite 75g Branco A9 = ', valor_sulfite75A9)
# print('Papel Sulfite 75g Branco A10 = ', valor_sulfite75A10)
# print(" ")
# print('Papel Fotográfico Glossy 180g', '----------------------------------')
# print('Papel Fotográfico Glossy 180g Branco A3 = ', valor_glossy130A3)
# print('Papel Fotográfico Glossy 180g Branco A4 = ', valor_glossy130A4)
# print('Papel Fotográfico Glossy 180g Branco A5 = ', valor_glossy130A5)
# print('Papel Fotográfico Glossy 180g Branco A6 = ', valor_glossy130A6)
# print('Papel Fotográfico Glossy 180g Branco A7 = ', valor_glossy130A7)
# print('Papel Fotográfico Glossy 180g Branco A8 = ', valor_glossy130A8)
# print('Papel Fotográfico Glossy 180g Branco A9 = ', valor_glossy130A9)
# print('Papel Fotográfico Glossy 180g Branco A10 = ', valor_glossy130A10)
# print(" ")
# print('Papel Fotográfico Glossy 230g', '----------------------------------')
# print('Papel Fotográfico Glossy 230g Branco A3 = ', valor_glossy230A3)
# print('Papel Fotográfico Glossy 230g Branco A4 = ', valor_glossy230A4)
# print('Papel Fotográfico Glossy 230g Branco A5 = ', valor_glossy230A5)
# print('Papel Fotográfico Glossy 230g Branco A6 = ', valor_glossy230A6)
# print('Papel Fotográfico Glossy 230g Branco A7 = ', valor_glossy230A7)
# print('Papel Fotográfico Glossy 230g Branco A8 = ', valor_glossy230A8)
# print('Papel Fotográfico Glossy 230g Branco A9 = ', valor_glossy230A9)
# print('Papel Fotográfico Glossy 230g Branco A10 = ', valor_glossy230A10)
# print(" ")
# print('Papel Fotográfico Matte 108g', '----------------------------------')
# print('Papel Fotográfico Matte 108g Branco A3 = ', valor_matte108A3)
# print('Papel Fotográfico Matte 108g Branco A4 = ', valor_matte108A4)
# print('Papel Fotográfico Matte 108g Branco A5 = ', valor_matte108A5)
# print('Papel Fotográfico Matte 108g Branco A6 = ', valor_matte108A6)
# print('Papel Fotográfico Matte 108g Branco A7 = ', valor_matte108A7)
# print('Papel Fotográfico Matte 108g Branco A8 = ', valor_matte108A8)
# print('Papel Fotográfico Matte 108g Branco A9 = ', valor_matte108A9)
# print('Papel Fotográfico Matte 108g Branco A10 = ', valor_matte108A10)
# print(" ")
