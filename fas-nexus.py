#this script takes a folder or list of fasta files and converts them to nexus format
import os
def readfasta(ficheiro):
    fich=open(ficheiro,"r")
    linhas=fich.readlines()
    tudo="".join(linhas)
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
a=os.getcwd()
b=os.listdir(a)
#or write the list of files you want to convert below and uncomment the next line
#b=["yourfile.fas","yourfile2.fas"]
for x in b:
    if ".fas" in x:
        f=readfasta(x)
        out=file(x.split(".fas")[0]+".nex","w")
        out.write("#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=")
        out.write(str(len(f))+" NCHAR="+str(len(f[0][1]))+";\n")
        out.write("FORMAT DATATYPE=DNA  MISSING=? GAP=- MATCHCHAR=.;\nMATRIX\n")
        lenames=[]
        for i in f:
            lenames.append(len(i[0]))
        for j in f:
            out.write(j[0]+" "*(max(lenames)-len(j[0])+1)+j[1].replace("N","?")+"\n")
        out.write(";\nEND;\n")
    
              

        
