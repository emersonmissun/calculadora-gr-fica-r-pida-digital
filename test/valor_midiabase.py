#! /bin/env python

# Script para carregar custos de papéis para impressão

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

# Importar bibliotecas e módulos necessários para o script funcionar corretamente 
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Carregar o arquivo de dados em excel com valor e tipos de papel para impressão

