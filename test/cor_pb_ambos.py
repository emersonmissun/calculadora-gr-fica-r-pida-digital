#! /usr/bin/env python3

# Selecionar tipo de impressão (colorida, preto e branco ou personalizada) e quantidade de cópias
from calcprint import tipo_impressao


def menu_qtd_paginas_tipo_impressao():
    qtd_paginas = {}

    # // Note: Qtds impressões coloridas
    qtd_paginas["print_img_cor"] = int(input("Quantidade de páginas inteiras com fotos coloridas: "))
    qtd_paginas["print_txt_img_cor"] = int(input("Quantidade de páginas inteiras com fotos e texto coloridos: "))
    qtd_paginas["print_txt_cor"] = int(input("Quantidade de páginas inteiras com texto colorido: "))
    # // Note: Qtds impressões PB
    qtd_paginas["print_img_pb"] = int(input("Quantidade de páginas inteiras com fotos preto e branco: "))
    qtd_paginas["print_txt_img_pb"] = int(input("Quantidade de páginas inteiras com fotos e texto preto e branco: "))
    qtd_paginas["print_txt_pb"] = int(input("Quantidade de páginas inteiras com texto preto e branco: "))
    return qtd_paginas

def menu_principal():
	print("Escolha o tipo de impressão:")
	print("1 - Colorida")
	print("2 - Preto e Branco")
	print("3 - Ambos")
	tipo_impressao = int(input("Digite a opção desejada: ")) # 1, 2 ou 3

if tipo_impressao == 1:
	print("Colorida") # Impressão colorida selecionada pelo usuário (1) 

elif tipo_impressao == 2:
	print("Preto e Branco") # Impressão preto e branco selecionada pelo usuário (2)
    
# Menu 3: Quantidade de páginas por tipo de impressão
elif tipo_impressao == "3":
        qtd_paginas_tipo_impressao = menu_qtd_paginas_tipo_impressao()
        print(qtd_paginas_tipo_impressao)

else: # Caso o usuário digite um valor diferente de 1, 2 ou 3
	print("Opção inválida")
