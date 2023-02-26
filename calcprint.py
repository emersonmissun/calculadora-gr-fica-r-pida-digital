#! /bin/env python3

# Menu para Selecionar tipo de impressão ([1] Colorida, [2] Preto e Branco, [3] Personalizar)
def menu_tipo_impressao():
	print("Selecione o tipo de impressão: ")
	print("[1] Colorida")
	print("[2] Preto e Branco")
	print("[3] Personalizar")
	tipo_impressao = int(input("Opção: "))
	return tipo_impressao

print(menu_tipo_impressao())

## Exibir a opção de tipo de impressão selecionada e retornar o valor da opção escolhida ##
def tipo_impressao(tipo_impressao):
	if tipo_impressao == 1:
		print("Tipo de impressão selecionado: Colorida")
		return tipo_impressao
	elif tipo_impressao == 2:
		print("Tipo de impressão selecionado: Preto e Branco")
		return tipo_impressao
	elif tipo_impressao == 3:
		print("Tipo de impressão selecionado: Personalizar")
		return tipo_impressao
	else:
		print("Opção inválida!")
		return 0
