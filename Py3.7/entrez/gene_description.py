import pandas as pd
from Bio import Entrez

Entrez.email = 'scdyao@gmail.com'

df = pd.read_excel(r'C:\Users\sc-dyao\Desktop\REHS-2019\Py3.7\entrez\gene_result.xlsx')

string = ''
for gene in df['Symbol']:
    string += (gene + ',')

entData = Entrez.fetch(db='gene', id=string, retmode=text)
