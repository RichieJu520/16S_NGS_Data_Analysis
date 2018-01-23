import random
from Bio import SeqIO

print 'Function: This script is written for random extracting of N seqs from fasta'
while True:
    Paras=raw_input("Enter two parameters: [Fasta],[Num] sepeated by Space: ")
    try:
        filename=Paras.split(' ')[0]
        N=int(Paras.split(' ')[1])
        break
    except:
        continue
    
from Bio import SeqIO 
fileinput =open(filename,'r')
fileoutput=open(filename+'_Random_'+str(N),'w')

print 'The Python script is running... Pls wait!'

a=[]
i=0
for record in SeqIO.parse(filename,'fasta'):
    a.append('>'+str(record.description)+'\n'+str(record.seq)+'\n')
print len(a)

b=random.sample(a, N)
for item in b:
    fileoutput.write(item)

print 'OK, Finished!'
raw_input("Press <Enter> to close this window: ")
