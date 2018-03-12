def readfasta(ficheiro):
    fich=open(ficheiro,"r")
    linhas=fich.readlines()
    tudo="".join(linhas).replace("\r","")
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
a=os.getcwd()
b=os.listdir(a)
for x in b:
    if ".fas" in x:
        f=readfasta(x)
        l=len(f)
        sl=len(f[0][1])
        o=file(x.split(".fas")[0]+".phy","w")
        o.write(" "+str(l)+" "+str(sl)+"\n")
        for seq in f:
            o.write(seq[0]+" "*(13-len(seq[0])))
            for bl50 in range(sl/50):
                for bl10 in range(5):
                    for p in range(10):
                        o.write(seq[1][bl50*50+bl10*10+p])
                    o.write(" ")
                o.write("\n             ")
            jata=sl/50*50
            falta=sl-jata
            for blo10 in range(falta/10):
                for pos in range(10):
                    o.write(seq[1][jata+blo10*10+pos])
                o.write(" ")
            jata=jata+falta/10*10
            for mis in range(sl-jata):
                o.write(seq[1][jata+mis])
            o.write("\n")
        o.close()







