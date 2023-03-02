#! /bin/env python3

# Preço de impressão colorida e preto e branco por formato de papel A3, A4 e A5

# Importar bibliotecas e módulos necessários para o script funcionar corretamente 
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Carregar o arquivo de dados em excel com valor e tipos de impressão
valor_cor = pd.read_excel('data/Dados_Entrada/expenses/impressao_custos.xlsx', sheet_name='cor', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), nrows=3)
valor_pb = pd.read_excel('data/Dados_Entrada/expenses/impressao_custos.xlsx', sheet_name='pb', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), nrows=3)

# print(valor_cor)	# Exibe os valores de impressão colorida na tela do terminal 
# print(valor_pb)	# Exibe os valores de impressão preto e branco na tela do terminal

## NOTE: Valores de impressão cor formato A3 
valor_img_cor_a3 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A3'].item() 
valor_img_cor_a3 = locale.currency(valor_img_cor_a3, grouping=True)

valor_txt_cor_a3 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A3'].item()
valor_txt_cor_a3 = locale.currency(valor_txt_cor_a3, grouping=True)

valor_txt_img_cor_a3 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A3'].item()
valor_txt_img_cor_a3 = locale.currency(valor_txt_img_cor_a3, grouping=True)

## NOTE: Valores de impressão PB formato A3
valor_img_pb_a3 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A3_PB'].item()
valor_img_pb_a3 = locale.currency(valor_img_pb_a3, grouping=True)

valor_txt_pb_a3 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A3_PB'].item()
valor_txt_pb_a3 = locale.currency(valor_txt_pb_a3, grouping=True)

valor_txt_img_pb_a3 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A3_PB'].item()
valor_txt_img_pb_a3 = locale.currency(valor_txt_img_pb_a3, grouping=True)

## NOTE: Valores de impressão cor formato A4 
valor_img_cor_a4 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A4'].item()  
valor_img_cor_a4 = locale.currency(valor_img_cor_a4, grouping=True)

valor_txt_cor_a4 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A4'].item()
valor_txt_cor_a4 = locale.currency(valor_txt_cor_a4, grouping=True)

valor_txt_img_cor_a4 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A4'].item()
valor_txt_img_cor_a4 = locale.currency(valor_txt_img_cor_a4, grouping=True)

## NOTE: Valores de impressão PB formato A4
valor_img_pb_a4 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A4_PB'].item()
valor_img_pb_a4 = locale.currency(valor_img_pb_a4, grouping=True)

valor_txt_pb_a4 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A4_PB'].item()
valor_txt_pb_a4 = locale.currency(valor_txt_pb_a4, grouping=True)

valor_txt_img_pb_a4 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A4_PB'].item()
valor_txt_img_pb_a4 = locale.currency(valor_txt_img_pb_a4, grouping=True)

## NOTE: Valores de impressão cor formato A5
valor_img_cor_a5 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A5'].item()
valor_img_cor_a5 = locale.currency(valor_img_cor_a5, grouping=True)

valor_txt_cor_a5 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A5'].item()
valor_txt_cor_a5 = locale.currency(valor_txt_cor_a5, grouping=True)

valor_txt_img_cor_a5 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A5'].item()
valor_txt_img_cor_a5 = locale.currency(valor_txt_img_cor_a5, grouping=True)

## NOTE: Valores de impressão PB formato A5
valor_img_pb_a5 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A5_PB'].item()
valor_img_pb_a5 = locale.currency(valor_img_pb_a5, grouping=True)

valor_txt_pb_a5 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A5_PB'].item()
valor_txt_pb_a5 = locale.currency(valor_txt_pb_a5, grouping=True)

valor_txt_img_pb_a5 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A5_PB'].item()
valor_txt_img_pb_a5 = locale.currency(valor_txt_img_pb_a5, grouping=True)

## NOTE: Valores de impressão cor formato A6
valor_img_cor_a6 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A6'].item()
valor_img_cor_a6 = locale.currency(valor_img_cor_a6, grouping=True)

valor_txt_cor_a6 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A6'].item()
valor_txt_cor_a6 = locale.currency(valor_txt_cor_a6, grouping=True)

valor_txt_img_cor_a6 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A6'].item()
valor_txt_img_cor_a6 = locale.currency(valor_txt_img_cor_a6, grouping=True)

## NOTE: Valores de impressão PB formato A6
valor_img_pb_a6 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A6_PB'].item()
valor_img_pb_a6 = locale.currency(valor_img_pb_a6, grouping=True)

valor_txt_pb_a6 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A6_PB'].item()
valor_txt_pb_a6 = locale.currency(valor_txt_pb_a6, grouping=True)

valor_txt_img_pb_a6 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A6_PB'].item()
valor_txt_img_pb_a6 = locale.currency(valor_txt_img_pb_a6, grouping=True)

## NOTE: Valores de impressão cor formato A7
valor_img_cor_a7 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A7'].item()
valor_img_cor_a7 = locale.currency(valor_img_cor_a7, grouping=True)

valor_txt_cor_a7 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A7'].item()
valor_txt_cor_a7 = locale.currency(valor_txt_cor_a7, grouping=True)

valor_txt_img_cor_a7 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A7'].item()
valor_txt_img_cor_a7 = locale.currency(valor_txt_img_cor_a7, grouping=True)

## NOTE: Valores de impressão PB formato A7
valor_img_pb_a7 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A7_PB'].item()
valor_img_pb_a7 = locale.currency(valor_img_pb_a7, grouping=True)

valor_txt_pb_a7 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A7_PB'].item()
valor_txt_pb_a7 = locale.currency(valor_txt_pb_a7, grouping=True)

valor_txt_img_pb_a7 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A7_PB'].item()
valor_txt_img_pb_a7 = locale.currency(valor_txt_img_pb_a7, grouping=True)

## NOTE: Valores de impressão cor formato A8
valor_img_cor_a8 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A8'].item()
valor_img_cor_a8 = locale.currency(valor_img_cor_a8, grouping=True)

valor_txt_cor_a8 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A8'].item()
valor_txt_cor_a8 = locale.currency(valor_txt_cor_a8, grouping=True)

valor_txt_img_cor_a8 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A8'].item()
valor_txt_img_cor_a8 = locale.currency(valor_txt_img_cor_a8, grouping=True)

## NOTE: Valores de impressão PB formato A8
valor_img_pb_a8 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A8_PB'].item()
valor_img_pb_a8 = locale.currency(valor_img_pb_a8, grouping=True)

valor_txt_pb_a8 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A8_PB'].item()
valor_txt_pb_a8 = locale.currency(valor_txt_pb_a8, grouping=True)

valor_txt_img_pb_a8 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A8_PB'].item()
valor_txt_img_pb_a8 = locale.currency(valor_txt_img_pb_a8, grouping=True)

## NOTE: Valores de impressão cor formato A9
valor_img_cor_a9 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A9'].item()
valor_img_cor_a9 = locale.currency(valor_img_cor_a9, grouping=True)

valor_txt_cor_a9 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A9'].item()
valor_txt_cor_a9 = locale.currency(valor_txt_cor_a9, grouping=True)

valor_txt_img_cor_a9 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A9'].item()
valor_txt_img_cor_a9 = locale.currency(valor_txt_img_cor_a9, grouping=True)

## NOTE: Valores de impressão PB formato A9
valor_img_pb_a9 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A9_PB'].item()
valor_img_pb_a9 = locale.currency(valor_img_pb_a9, grouping=True)

valor_txt_pb_a9 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A9_PB'].item()
valor_txt_pb_a9 = locale.currency(valor_txt_pb_a9, grouping=True)

valor_txt_img_pb_a9 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A9_PB'].item()
valor_txt_img_pb_a9 = locale.currency(valor_txt_img_pb_a9, grouping=True)

## NOTE: Valores de impressão cor formato A10
valor_img_cor_a10 = valor_cor.loc[valor_cor['tipo'] == 'IMG_COR', 'PRINT_A10'].item()
valor_img_cor_a10 = locale.currency(valor_img_cor_a10, grouping=True)

valor_txt_cor_a10 = valor_cor.loc[valor_cor['tipo'] == 'TXT_COR', 'PRINT_A10'].item()
valor_txt_cor_a10 = locale.currency(valor_txt_cor_a10, grouping=True)

valor_txt_img_cor_a10 = valor_cor.loc[valor_cor['tipo'] == 'TXT_IMG_COR', 'PRINT_A10'].item()
valor_txt_img_cor_a10 = locale.currency(valor_txt_img_cor_a10, grouping=True)

## NOTE: Valores de impressão PB formato A10
valor_img_pb_a10 = valor_pb.loc[valor_pb['tipo_pb'] == 'IMG_PB', 'PRINT_A10_PB'].item()
valor_img_pb_a10 = locale.currency(valor_img_pb_a10, grouping=True)

valor_txt_pb_a10 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_PB', 'PRINT_A10_PB'].item()
valor_txt_pb_a10 = locale.currency(valor_txt_pb_a10, grouping=True)

valor_txt_img_pb_a10 = valor_pb.loc[valor_pb['tipo_pb'] == 'TXT_IMG_PB', 'PRINT_A10_PB'].item()
valor_txt_img_pb_a10 = locale.currency(valor_txt_img_pb_a10, grouping=True)

### Iniciar variáveis com preços de impressão colorida e preto e branco para cada formato de impressão ###
img_cor_ = {
	"A3": valor_img_cor_a3,
	"A4": valor_img_cor_a4,
	"A5": valor_img_cor_a5, 
	"A6": valor_img_cor_a6,
	"A7": valor_img_cor_a7,
	"A8": valor_img_cor_a8,
	"A9": valor_img_cor_a9,
	"A10": valor_img_cor_a10
}

txt_cor_ = {
    "A3": valor_txt_cor_a3,
    "A4": valor_txt_cor_a4,
    "A5": valor_txt_cor_a5,
    "A6": valor_txt_cor_a6,
    "A7": valor_txt_cor_a7,
    "A8": valor_txt_cor_a8,
    "A9": valor_txt_cor_a9,
    "A10": valor_txt_cor_a10
}

txt_img_cor = {
    "A3": valor_txt_img_cor_a3,
    "A4": valor_txt_img_cor_a4,
    "A5": valor_txt_img_cor_a5,
    "A6": valor_txt_img_cor_a6,
    "A7": valor_txt_img_cor_a7,
    "A8": valor_txt_img_cor_a8,
    "A9": valor_txt_img_cor_a9,
    "A10": valor_txt_img_cor_a10
}

img_pb = {
    "A3": valor_img_pb_a3,
    "A4": valor_img_pb_a4,
    "A5": valor_img_pb_a5,
    "A6": valor_img_pb_a6,
    "A7": valor_img_pb_a7,
    "A8": valor_img_pb_a8,
    "A9": valor_img_pb_a9,
    "A10": valor_img_pb_a10
}

txt_pb = {
    "A3": valor_txt_pb_a3,
    "A4": valor_txt_pb_a4,
    "A5": valor_txt_pb_a5,
    "A6": valor_txt_pb_a6,
    "A7": valor_txt_pb_a7,
    "A8": valor_txt_pb_a8,
    "A9": valor_txt_pb_a9,
    "A10": valor_txt_pb_a10
}

txt_img_pb = {
    "A3": valor_txt_img_pb_a3,
    "A4": valor_txt_img_pb_a4,
    "A5": valor_txt_img_pb_a5,
    "A6": valor_txt_img_pb_a6,
    "A7": valor_txt_img_pb_a7,
    "A8": valor_txt_img_pb_a8,
    "A9": valor_txt_img_pb_a9,
    "A10": valor_txt_img_pb_a10
}

## Exibir valores de impressão
# print("-------------------------------------------------------------------")
# print("Valores de impressão A3")
# print("Print Textos PB A3 =", valor_txt_pb_a3)
# print("Print Textos e Imagens PB A3 =", valor_txt_img_pb_a3)
# print("Print Foto PB A3 =", valor_img_pb_a3)
# print("")
# print("Print Textos Cor A3 =", valor_txt_cor_a3)
# print("Print Textos e Imagens Cor A3 =", valor_txt_img_cor_a3)
# print('Print Foto Cor A3 =', valor_img_cor_a3)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A4")
# print("Print Textos PB A4 =", valor_txt_pb_a4)
# print("Print Textos e Imagens PB A4 =", valor_txt_img_pb_a4)
# print("Print Foto PB A4 =", valor_img_pb_a4)
# print("")
# print("Print Textos Cor A4 =", valor_txt_cor_a4)
# print("Print Textos e Imagens Cor A4 =", valor_txt_img_cor_a4)
# print('Print Foto Cor A4 =', valor_img_cor_a4)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A5")
# print("Print Textos PB A5 =", valor_txt_pb_a5)
# print("Print Textos e Imagens PB A5 =", valor_txt_img_pb_a5)
# print("Print Foto PB A5 =", valor_img_pb_a5)
# print("")
# print("Print Textos Cor A5 =", valor_txt_cor_a5)
# print("Print Textos e Imagens Cor A5 =", valor_txt_img_cor_a5)
# print('Print Foto Cor A5 =', valor_img_cor_a5)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A6")
# print("Print Textos PB A6 =", valor_txt_pb_a6)
# print("Print Textos e Imagens PB A6 =", valor_txt_img_pb_a6)
# print("Print Foto PB A6 =", valor_img_pb_a6)
# print("")
# print("Print Textos Cor A6 =", valor_txt_cor_a6)
# print("Print Textos e Imagens Cor A6 =", valor_txt_img_cor_a6)
# print('Print Foto Cor A6 =', valor_img_cor_a6)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A7")
# print("Print Textos PB A7 =", valor_txt_pb_a7)
# print("Print Textos e Imagens PB A7 =", valor_txt_img_pb_a7)
# print("Print Foto PB A7 =", valor_img_pb_a7)
# print("")
# print("Print Textos Cor A7 =", valor_txt_cor_a7)
# print("Print Textos e Imagens Cor A7 =", valor_txt_img_cor_a7)
# print('Print Foto Cor A7 =', valor_img_cor_a7)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A8")
# print("Print Textos PB A8 =", valor_txt_pb_a8)
# print("Print Textos e Imagens PB A8 =", valor_txt_img_pb_a8)
# print("Print Foto PB A8 =", valor_img_pb_a8)
# print("")
# print("Print Textos Cor A8 =", valor_txt_cor_a8)
# print("Print Textos e Imagens Cor A8 =", valor_txt_img_cor_a8)
# print('Print Foto Cor A8 =', valor_img_cor_a8)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A9")
# print("Print Textos PB A9 =", valor_txt_pb_a9)
# print("Print Textos e Imagens PB A9 =", valor_txt_img_pb_a9)
# print("Print Foto PB A9 =", valor_img_pb_a9)
# print("")
# print("Print Textos Cor A9 =", valor_txt_cor_a9)
# print("Print Textos e Imagens Cor A9 =", valor_txt_img_cor_a9)
# print('Print Foto Cor A9 =', valor_img_cor_a9)
# print("-------------------------------------------------------------------")
# print("")

# print("Valores de impressão A10")
# print("Print Textos PB A10 =", valor_txt_pb_a10)
# print("Print Textos e Imagens PB A10 =", valor_txt_img_pb_a10)
# print("Print Foto PB A10 =", valor_img_pb_a10)
# print("")
# print("Print Textos Cor A10 =", valor_txt_cor_a10)
# print("Print Textos e Imagens Cor A10 =", valor_txt_img_cor_a10)
# print('Print Foto Cor A10 =', valor_img_cor_a10)
# print("-------------------------------------------------------------------")
# print("")
