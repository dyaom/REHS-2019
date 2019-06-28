inFile = open('clinvar_result.txt', 'r')
outFile = open('clinvar_processed.txt', 'w')

for line in inFile:
    if line.split('\t')[0][-1]==')':
        outFile.write(line)

inFile.close()
outFile.close()
        
