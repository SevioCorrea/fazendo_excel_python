import pandas

# Faz um Dicionário com os itens
redes_sociais = {
    'Donos': ['Microsoft', 'Google', 'Meta'],
    'Redes': ['LinkedIn', 'YouTube', 'Facebook'],
    'Fundação': ['2002', '2005', '2004'],
}
# Lendo os dados e fazendo o Arquivo
dataframe = pandas.DataFrame(redes_sociais)
dataframe.to_excel('./redes_sociais.xlsx')



                    'https://www.linkedin.com/in/seviocorrea/'