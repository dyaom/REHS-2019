import pandas as pd
from Bio import Entrez
from Bio import SeqIO

print('import done')

Entrez.email = 'scdyao@gmail.com'

df = pd.read_excel(r'C:\Users\sc-dyao\Desktop\REHS-2019\Py3.7\entrez\gene_result.xlsx')

string = ''
for gene in df['GeneID']:
    string += (str(gene) + ',')

#string = '21,26090,79611,8754,54507'

#print(string)
#raise SystemExit

entFile = Entrez.efetch(db='gene', id=string)
print('fetched data')
entData = entFile.read()
print('read data')

output = open('gene_containsCataract.txt', 'w')
newGeneStart = 0
newGeneEnd = 0
while newGeneEnd != -1:
    newGeneEnd = entData.find('Entrezgene', newGeneStart+1)
    if entData[newGeneStart:newGeneEnd].find('cataract') != -1:
        status = 'YES'
    else:
        status = 'no'
    output.write(status + '\n')
    newGeneStart = newGeneEnd
output.close()
