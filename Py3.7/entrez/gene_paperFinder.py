import pandas as pd
from Bio import Entrez
from Bio import SeqIO

print('import done')

QUERY = 'cataract'
MAX_NUM = 8

Entrez.email = 'scdyao@gmail.com'

df = pd.read_excel(r'C:\Users\sc-dyao\Desktop\REHS-2019\Py3.7\entrez\gene_result.xlsx')

#get already processed genes
doneGenes = []
out = open('gene_relevantPapers.txt', 'r')
for line in out:
    doneGenes.append(line.split('\t')[0])
out.close()
                     

for gene in df['Symbol']:
    if gene not in doneGenes:
        query = gene + ' ' + QUERY
        print(query)
        entHandle = Entrez.esearch(db='pubmed', term=query, usehistory='y')
        entData = Entrez.read(entHandle)
        count = 0
        if len(entData['IdList']) == 0:
            output = open('gene_relevantPapers.txt', 'a')
            output.write(gene)
            output.write('\t')
            output.write('none')
            output.write('\n')
            output.close()
        else:
            print(len(entData['IdList']))
            for pmid in entData['IdList']:
                print(pmid)
                fetch_handle = Entrez.efetch(db="pubmed",
                                             id=pmid)
                data = fetch_handle.read()
                start = data.find('abstract "')+9
                end = data.find('",\n', start)
                print(data[start:end])
                yn = ''
                while yn not in ['y', 'n']:
                    yn = input('relevant: ')
                    if yn == 'y':
                        output = open('gene_relevantPapers.txt', 'a')
                        output.write(gene)
                        output.write('\t')
                        output.write(pmid)
                        output.write('\n')
                        output.close()
                if yn == 'y':
                    break
                else:
                    count += 1
                    if count > MAX_NUM:
                        output = open('gene_relevantPapers.txt', 'a')
                        output.write(gene)
                        output.write('\t')
                        output.write('not relevant')
                        output.write('\n')
                        output.close()
                        break
            else:
                output = open('gene_relevantPapers.txt', 'a')
                output.write(gene)
                output.write('\t')
                output.write('not relevant')
                output.write('\n')
                output.close()
        
        

'''
entFile = Entrez.efetch(db='gene', id=string)

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
'''
