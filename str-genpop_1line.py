#converts structure files (1 line format, separated by tabs, first line is the individual identifier and the second the pop indentifier) into genepop files
#it converts batches of files or individual files. In the latter case uncomment the definition of y as a list
#IMPORTANT: structure files need to be called ".str"
#Are the first line of the structure files the loci names? if yes, choose 1 in the next line, if not choose 0
genstart=1
import os
u=os.getcwd()
y=os.listdir(u)
#y=["yourfile1.str","yourfile2.str"]

for ficheiro in y:
    if ".str" in ficheiro:

        fich=file(ficheiro,"r")
        linhas=fich.read().split("\n")
        out=file(ficheiro.split(".str")[0]+".gen","w")
        nloc=(len(linhas[1].split("\t"))-2)/2
        fich.close()
        out.write("your_comment_line\n")
        if genstart==1:
            locnames=[]
            for lo in linhas[0].split("\t"):
                if lo!="":
                    locnames.append(lo)
            out.write(locnames[0])
            for loc in locnames[1:]:
                out.write(", "+loc)
        else:
            out.write("loc1")
            for i in range(nloc-1):
                out.write(", loc"+str(i+2))
        
        lines=[]
        poplist=[]
        out.write("\n")
        for t in linhas[genstart:]:
            if t!="":
                if t!=" ":
                    lines.append(t)
                    popn=t.split("\t")[1]
                    if popn not in poplist:
                        poplist.append(popn)
        
        teste=3
        z =lines[1].split("\t")[teste]
        while z=="-9":
            teste+=1
            z=lines[1].split("\t")[teste]
            
        ndig=len(z)
        

        npops=len(poplist)
        for pop in poplist:
            out.write("pop\n")
            for l in lines:
                a=l.split("\t")
                if a[1]==pop:
                    #note that some programs require " ,  " instead of ", ". Change if needed below.
                    out.write(a[0]+",")
                    for x in range(nloc):
                        if a[2*x+2]=="-9":
                            out.write(" "+ndig*"0")
                        else:
                            out.write(" "+a[2*x+2])
                        if a[2*x+3]=="-9":
                            out.write(ndig*"0")
                        else:
                            out.write(a[2*x+3])
                    out.write("\n")
        out.close()
                    
