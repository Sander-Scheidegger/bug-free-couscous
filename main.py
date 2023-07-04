# Primeiro exercício:
# Quero que crie em python um programa que armazene os dados de usuários em um csv 
# Dados do usuário: 
#   Nome
#   Idade 
#   Sexo
#   Nacionalidade 
#   CPF 
# Esses dados devem ser gerados de forma aleatória.

#Importação de bibliotecas
import numpy as np
import pandas as pd

#Lista com lista de palavras:
nome_lista = ['Sander', 'Pedro', 'André', 'Camila', 'Samuel', 'Carlos','James']
sobrenome_lista = ['Araújo', 'Moraes', 'da Costa', 'da Silva', 'Paulo', 'bond']
nacionalidade_lista = ['Acreano', 'amapaense', 'alagoano' 'amazonense', 'baiano', 'cearense', 'brasiliense', 'capixaba', 'goiano', 'maranhese',
                       'mato-grossense', 'mineiro', 'paraense', 'paraibano', 'paranaense', 'pernambucano', 'piauiense', 'fluminense', 'potiguar', 'gaucho', 'rondoniano', 'roraimense'
                       'catarinense', 'paulista', 'sergipano', 'tocantinense']

#Seleção aleatória
idade = np.random.randint(1, 101)

rand = np.random.randint(1,101)
if rand % 2 == 0:
    sexo = 'M'
else:
    sexo = 'F'

rand = np.random.randint(1,7)
nome = nome_lista[rand]

rand = np.random.randint(1,6)
sobrenome = sobrenome_lista[rand]

rand = np.random.randint(1,26)
nacionalidade = nacionalidade_lista[rand]

#Formatação do CPF para o formato "xxx.xxx.xxx-xx"
rand = np.random.randint(10000000, 1000000000) # 020.668.371-56
cpf_cru = str(rand)
digito_verificador = str(np.random.randint(10,99))
cpf_formatado = "{}.{}.{}-{}".format(cpf_cru[:3], cpf_cru[3:6], cpf_cru[6:9], digito_verificador[:2])

#conversão para
pessoa = [nome, sobrenome, idade, sexo, nacionalidade, cpf_formatado]
df = pd.DataFrame(pessoa)
df.to_csv("CSV com Pessoas Aleatórias", header=False, index=False)
