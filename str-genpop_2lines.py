#converts structure files into genepop format
#the expected structure format are 2 lines per individual, first two columns separated by tabs, genotype data separated by spaces).
#first line is the individual identifier and the second the pop indentifier
#it converts batches of files or individual files. In the latter case uncomment the definition of y as a list
#IMPORTANT: structure files need to be called ".str"
#Are the first line of the structure files the loci names? if yes, choose 1 in the next line, if not choose 0
genstart=1
import os
u=os.getcwd()
y=os.listdir(u)

#y=["yourfilename1","yourfilename2"]

for ficheiro in y:
    if ".str" in ficheiro:
        fich=file(ficheiro,"r")
        linha=fich.read()
        linhas=linha.split("\n")
        out=file(ficheiro.split(".str")[0]+".gen","w")
        nloc=len(linhas[1].split("\t")[2].split(" "))
        loci=[]
        if genstart==1:
            a=linhas[0].split("\t")
            for l in a:
                if l!="":
                    u=l.split(" ")
                    for locit in u:
                        loci.append(l.replace("\t","").replace(" ",""))
        else:
            for x in range(nloc):
                loci.append("loc"+str(x))
            
        
        fich.close()
        out.write("your_comment_line\n")
        out.write(loci[0])
        for i in loci[1:]:
            out.write(", "+i)
        lines=[]
        poplist=[]
        out.write("\n")
        for t in linhas[genstart:]:
            if t!="":
                if t!=" ":
                    lines.append(t.split("\t"))
                    popn=t.split("\t")[1]
                    if popn not in poplist:
                        poplist.append(popn)
        teste=3
        z =lines[3][2].split(" ")[teste]
        while z=="-9":
            teste+=1
            z=lines[3][2].split(" ")[teste]
            
        ndig=len(z)


        npops=len(poplist)
        for pop in poplist:
            out.write("pop\n")
            for l in range(len(lines)/2):
                if lines[2*l][1]==pop:
                    #some programs require " , " instead of ",". Change if needed.
                    out.write(lines[2*l][1]+lines[2*l][0]+",")
                    for x in range(nloc):
                        if lines[2*l][2].split(" ")[x]=="-9":
                            out.write(" " + ndig*"0")
                        else:
                            out.write(" "+lines[2*l][2].split(" ")[x])
                        if lines[2*l+1][2].split(" ")[x]=="-9":
                            out.write(ndig*"0")
                        else:
                            out.write(lines[2*l+1][2].split(" ")[x])
                    out.write("\n")
        out.close()
                
