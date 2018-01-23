print 'Function: This script is written to randomly extract [N] sequences from each fasta of [FolderName]!'

import random
from Bio import SeqIO
import os

def making_folder(foldername):
    if os.path.exists(foldername):
        for root, dirs, files in os.walk(foldername):
            for name in files:
                os.remove(os.path.join(root,name))
    else:
        os.mkdir(foldername)

while True:
    Paras=raw_input("Enter two parameters: [FolderName],[Num] sepeated by Space: ")
    try:
        foldername=Paras.split(' ')[0]
        N=int(Paras.split(' ')[1])
        break
    except:
        continue


making_folder(foldername+'.Random'+str(N)+'.sequences')

for root,dirs,files in os.walk(foldername):
    for file in files:
        print '------','Processing',file,'in prograss','------'
        fileoutput=open(foldername+'.Random'+str(N)+'.sequences'+'/'+file.replace('.fasta','')+'_Random_'+str(N)+'.fasta','w')
        a=[]
        i=0
        for record in SeqIO.parse(os.path.join(root, file), 'fasta'):
            i+=1
            a.append('>'+str(record.description)+'\n'+str(record.seq)+'\n')
        try:
            b=random.sample(a, N)
            print 'OK, random extraction of',N,'sequences finished!'
        except:
            b=random.sample(a, i)
            print file,'has only',str(i),'seqs, which is less than the setup value',N
            print 'OK, random extraction of',i,'sequences finished!'  
        for item in b:
            fileoutput.write(item)

print 'OK, Finished!'
raw_input("Press <Enter> to close this window: ")
