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

output = open('gene_summaries.txt', 'w')
newGeneStart = 0
newGeneEnd = 0
while newGeneEnd != -1:
    newGeneEnd = entData.find('Entrezgene', newGeneStart+1)
    startInd = entData.find('summary "', newGeneStart, newGeneEnd)
    if startInd == -1:
        summary = ""
    else:
        endInd = entData.find('"', startInd+9)
        summary = entData[startInd+9:endInd].replace('\n', '')
    output.write(summary + '\n')
    newGeneStart = newGeneEnd
output.close()
