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
nome_homem_lista = ['Sander', 'Pedro', 'André', 'Samuel', 'Carlos','James', 'Moisés', 'Felipe', 'Luciano', 'Diego']
nome_mulher_lista = ['Sandra', 'Patritcia', 'Andreia', 'Samara', 'Carla','Jenifer', 'Monica', 'Thaynara', 'Michele', 'Leticia']
sobrenome_lista = ['Araújo', 'Moraes', 'da Costa', 'da Silva', 'Paulo', 'Bond', 'Pereira', 'Macedo', 'Pinto']
nacionalidade_lista = ['acreano', 'amapaense', 'alagoano', 'amazonense', 'baiano', 'cearense', 'brasiliense', 'capixaba', 'goiano', 'maranhese',
                       'mato-grossense', 'mineiro', 'paraense', 'paraibano', 'paranaense', 'pernambucano', 'piauiense', 'fluminense', 'potiguar', 'gaucho', 'rondoniano', 'roraimense',
                       'catarinense', 'paulista', 'sergipano', 'tocantinense']#26 itens

#Seleção aleatória
def criarPessoa():
    idade = np.random.randint(1, 101)

    rand = np.random.randint(1,101)
    if rand % 2 == 0:
        sexo = 'M'
        rand = np.random.randint(1,10)
        nome = nome_homem_lista[rand]
    else:
        sexo = 'F'
        rand = np.random.randint(1,10)
        nome = nome_mulher_lista[rand]

    rand = np.random.randint(1,6)
    sobrenome = sobrenome_lista[rand]

    rand = np.random.randint(1,25)
    nacionalidade = nacionalidade_lista[rand]
    
    #Formatação do CPF para o formato "xxx.xxx.xxx-xx"
    rand = np.random.randint(100000000, 1000000000)
    cpf_cru = str(rand)
    digito_verificador = str(np.random.randint(10,99))
    cpf_formatado = "{}.{}.{}-{}".format(cpf_cru[:3], cpf_cru[3:6], cpf_cru[6:9], digito_verificador[:2])
    return nome, sobrenome, idade, sexo, nacionalidade, cpf_formatado


qntd = int(input('Digite quantas pessoas deseja criar: '))
pessoas = []
for i in range(qntd-1):
    pessoas.append(criarPessoa())

#conversão para .CSV
df = pd.DataFrame(
    pessoas,
    columns=["Nome", "Sobrenome", "idade", "Sexo", "Naturalidade", "CPF"]
    )
df.to_csv("CSV com Pessoas Aleatórias", header=False, index=False)

# #Criação do arquivo .XLSX
df.to_excel("Arquivo Excel.xlsx", engine="openpyxl", index=False)