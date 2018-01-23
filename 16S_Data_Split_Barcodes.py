import os
print 'This script is used to de-muticomplex 454 prosequences using barcode.map and with quality control!'
from Bio import SeqIO

while True:
    Parameters=raw_input("Enter five parameters: 1.[Fasta_name],2.[barcode.map],3.[Barcode_length](default:6),4.[Max_ambiguous](default:0) and 5.[Min_seq_length](default:50) sepeated by Space: ")
    try:
        file_name1=Parameters.strip().split(' ')[0]
        Map=Parameters.strip().split(' ')[1]
        N1=int(Parameters.strip().split(' ')[2])
        N2=int(Parameters.strip().split(' ')[3])
        N3=int(Parameters.strip().split(' ')[4])
        break
    except:
         print 'errors: invalid input format or not enough input !'
         continue

print 'Spliting fasta by barcodes...'
if os.path.exists(file_name1+'.separated'):
    for root, dirs, files in os.walk(file_name1+'.separated'):
        for name in files:
            os.remove(os.path.join(root,name))
else:
    os.mkdir(file_name1+'.separated')

handle=open(file_name1,'r')

a={}
for line in open(Map,'r'):
    if '#' not in line and len(line.rstrip().split('\t'))>=2:
        a[line.rstrip().split('\t')[1]]=line.rstrip().split('\t')[0]
    else:
        continue

Num, i, j =0, 0 , 0
Blist = []
for record in SeqIO.parse(handle,'fasta'):
    Num+=1
    Barcode = str(record.seq)[:N1]
    if Barcode in a.keys() and str(record.seq).count('N')<=N2 and len(str(record.seq))>=N3:
        Blist.append(Barcode)
        i+=1
        fileoutput = open(file_name1+'.separated'+'/'+a[Barcode]+'_'+Barcode+'.fasta','a')
        fileoutput.write('>'+str(record.description)+'\n')
        fileoutput.write(str(record.seq)[N1:]+'\n')
    else:
        j+=1
        fileoutput1=open(file_name1+'.separated'+'/'+'Others.fasta','a')
        fileoutput1.write('>'+str(record.description)+'\n')
        fileoutput1.write(str(record.seq)+'\n')     
    if Num%100000==0:
        print Num, 'sequences have been searched!'
print Num, 'sequences in total!'
print j,'sequecnes can NOT be assigned by Barcodes!'


UBlist = list(set(Blist))
result2=open(file_name1.replace('.fasta','')+'.log.txt','w')
for item in UBlist:
    result2.write(a[item]+'\t'+item+'\t'+str(Blist.count(item))+'\n')
    print 'Sample',a[item],item,str(Blist.count(item)),'sequences!'
                 
handle.close()
print 'OK, Finished!'
raw_input("Press <Enter> to close this window: ")
