File = open("TTN_in.txt",'r')
out = open('TTN_out.txt','w')

for line in File:
    items = line.rstrip().split('\t')
    for item in items:
        out.write(item + '\n')

File.close()
out.close()
