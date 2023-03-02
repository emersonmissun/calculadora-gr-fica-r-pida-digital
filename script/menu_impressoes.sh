#! /bin/env bash

# Selecionar tipo de impressão (colorida, preto e branco ou personalizada)
echo "Selecione o tipo de impressão:"
echo "1 - Colorida"
echo "2 - Preto e Branco"
echo "3 - Personalizada"
read -r tipo_impressao
echo " "
case $tipo_impressao in
  1) # Impressão colorida
    echo "A impressão será colorida"
	echo " "
    echo "Deseja imprimir frente e verso? (S/N)"
    read -r duplex
	echo " "

    if [[ $duplex == "S" || $duplex == "s" ]]; then
      echo "A impressão será frente e verso"
    else
      echo "A impressão será somente frente"
    fi

	echo " "
    echo "Quantas páginas terá o documento?"
    read -r qtd_paginas
   	echo " "
	echo "O documento terá $qtd_paginas impressão(ões)"

    ;;
  2)
    # Impressão preto e branco
    echo "A impressão será preto e branco"
	echo " "
    echo "Deseja imprimir frente e verso? (S/N)"
    read -r duplex
	echo " "

    if [[ $duplex == "S" || $duplex == "s" ]]; then
      echo "A impressão será frente e verso"
    else
      echo "A impressão será somente frente"
    fi

	echo " "
	echo "Quantas páginas terá o documento?"
    read -r qtd_paginas
    echo "O documento terá $qtd_paginas impressão(ões)"

    ;;
  3)
    # Impressão Personalizada
    echo "A impressão será personalizada"
	echo " "
	echo "Deseja imprimir frente e verso? (S/N)"
	read -r duplex
	echo " "

	if [[ $duplex == "S" || $duplex == "s" ]]; then
	echo "A impressão será frente e verso"
	else
	echo "A impressão será somente frente"
	fi

	echo " "
	echo "Quantas páginas inteiras com fotos coloridas terá o documento?" 
	read -r qtd_print_img_cor
	qtd_print_img_cor=$((qtd_print_img_cor))

	echo " "
	echo "Quantas páginas com textos e imagens coloridas terá o documento?"
	read -r qtd_print_text_img_cor
	qtd_print_text_img_cor=$((qtd_print_text_img_cor))

	echo " "
	echo "Quantas páginas com apenas textos coloridos terá o documento?"
	read -r qtd_print_text_cor
	qtd_print_text_cor=$((qtd_print_text_cor))

	echo " "
	echo "Quantas páginas inteiras com fotos preto e branco terá o documento?"
	read -r qtd_print_img_pb
	qtd_print_img_pb=$((qtd_print_img_pb))

	echo " "
	echo "Quantas páginas com textos e imagens preto e branco terá o documento?"
	read -r qtd_print_text_img_pb
	qtd_print_text_img_pb=$((qtd_print_text_img_pb))

	echo " "
	echo "Quantas páginas com apenas textos preto e branco terá o documento?"
	read -r qtd_print_text_pb
	qtd_print_text_pb=$((qtd_print_text_pb))

	echo " "
	echo "Quantidade total de páginas: $((qtd_print_img_cor+qtd_print_text_img_cor+qtd_print_text_cor+qtd_print_img_pb+qtd_print_text_img_pb+qtd_print_text_pb))"
	
	echo " "
	echo "Sendo:"
	echo "$((qtd_print_img_cor)) impressão(ões) inteira(s) com fotos coloridas"
	echo "$((qtd_print_text_img_cor)) impressão(ões) com textos e imagens coloridas"
	echo "$((qtd_print_text_cor)) impressão(ões) com apenas textos coloridos"
	echo "$((qtd_print_img_pb)) impressão(ões) inteira(s) com fotos preto e branco"
	echo "$((qtd_print_text_img_pb)) impressão(ões) com textos e imagens preto e branco"
	echo "$((qtd_print_text_pb)) impressão(ões) com apenas textos preto e branco"

	# // ToDo: Perguntar quantas cópias de apostilas serão impressas
    ;;
  *)
    echo "Opção inválida"
    ;;
esac 

