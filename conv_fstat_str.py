#this function converts data files from the FSTAT format into structure 1 line per individual format, no loci names
def fstat_str(fich):
    a=file(fich,"r")
    b=a.read()
    a.close()
    t=b.split("\n")
    if "\t" in t[0]:
        nl=int(t[0].split("\t")[1])
        nd=int(t[0].split("\t")[3])
    else:
        nl=int(t[0].split(" ")[1])
        nd=int(t[0].split(" ")[3])
    l=[]
    ind=1
    for linha in t[(nl+1):]:
        if linha not in ["","\t","\n"," "]:
            u=linha.split("\t")
            m=[]
            m.append(str(ind))
            m.append(u[0].replace(" ",""))
            for loc in range(nl):
                m.append(u[loc+1][:nd])
                m.append(u[loc+1][nd:])
            l.append(m)
            ind+=1
    return l
#to convert a batch of ".dat" files, place the script in the same folder as the files; new files called ".str" instead of ".dat" will be generated
import os
x=os.getcwd()
y=os.listdir(x)
for f in y:
    if ".dat" in f:
        out=file(f.split(".dat")[0]+".str","w")
        for l in fstat_str(f):
            out.write("\t".join(l)+"\n")
        out.close()

                
            
            
       
