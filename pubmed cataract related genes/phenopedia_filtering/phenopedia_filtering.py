pheno = []
with open('pheno_in.txt', 'r') as File:
    for line in File:
        pheno.append(line.rstrip().upper().split('\t')[0])
genes = []
with open('genes_in.txt', 'r') as File:
    for line in File:
        genes.append(line.rstrip().upper().replace(',', '\t').replace(' ', '').split('\t'))
        print(genes[-1])

print(len(pheno))
print(len(genes))

with open('genes_out.txt', 'w') as File:
    for gene in genes:
        for name in gene:
            if name in pheno:
                File.write('yes\n')
                break
        else:
            File.write('no\n')
