#builds IM data sets for pairs of species in the file pairs.txt (each pair in a line, species in pairs separated by tab)
#takes as input a series of fasta files, one per locus
#sequence names must include species id and different parts have to be separated by "_"
#seqid is in which part of the sequence name (start counting in 0):
seqid=2
#seqname is in which part of the sequence name (start counting in 0):
seqname=1
def readfasta(ficheiro):
    fich=file(ficheiro,"r")
    linhas=fich.readlines()
    tudo="".join(linhas)
    fich.close()
    split=tudo.split(">")[1:]
    seqs=[]
    for i in split:
        seq=[]
        a=i.split("\n")
        seq.append(a[0])
        b="".join(a[1:])
        b=b.upper()
        seq.append(b)
        seqs.append(seq)
    return seqs

import os
pairs=file("pairs.txt","r")
linhas=pairs.read()
lista=linhas.split("\n")
a=os.getcwd()
b=os.listdir(a)

for u in lista:
    par=u.split("\t")[:2]
    sp1=par[0]
    sp2=par[1]
    loc=[]
    for f in b:
        if ".fas" in f:
            x=readfasta(f)
            s1=[]
            s2=[]
            for s in x:
                try:
                    if s[0].split("_")[seqid]==sp1:
                        s1.append(s)
                    if s[0].split("_")[seqid]==sp2:
                        s2.append(s)
                except IndexError:
                    pass
            if len(s1)!=0:
                if len(s2)!=0:
                    loc.append([f.split(".fas")[0],s1,s2])
    o=file(sp1+"_"+sp2+"_im.u","w")
    o.write(sp1+"\t"+sp2+"\n# test\n2\n"+sp1+"  "+sp2+"  \n(0,1):2\n"+str(len(loc))+"\n")
    for l in loc:      
        o.write(l[0]+"  "+str(len(l[1]))+"  "+str(len(l[2]))+"  "+str(len(l[1][0][1]))+"  H  1.0\n")
        for seq in l[1]+l[2]:
            x=seq[0].split("_")[seqname]
            a=seq[1]
            for u in ["?","Y","W","R","K","S","M"]:
                a=a.replace(u,"N")         
            o.write(x+" "*(10-len(x))+a+"\n")
    o.close()
            
        
        

        
