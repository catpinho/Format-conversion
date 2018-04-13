#converts a batch of files from the genpop to structure (1 line per individual) format; this script needs to be in the same folder as the files to convert and genpop files need to be named ".gen"
#loci names, if present, will be ignored (the structure formatted file will have no locus name line)
#individual names will be preserved, populations will be named sequentially starting in "1"
import os
a=os.getcwd()
b=os.listdir(a)
for i in b:
    if ".gen" in i:
        c=file(i,"r")
        d=c.read()
        if "pop" in d:
            e=d.split("pop\n")
        elif "Pop" in d:
            e=d.split("Pop\n")
        elif "POP" in d:
            e=d.split("POP\n")
        out=file(i.split(".gen")[0]+".str","w")
        for pop in e[1:]:
            p=e.index(pop)
            x=pop.split("\n")
            for ind in x:
                if ind!= "":
                    o=ind.split(" ")
                    out.write(o[0].split(",")[0]+"\t"+str(p))
                    for loc in o[1:]:
                        if loc!="":
                            if loc[:(len(loc)/2)] not in ["0","00","000"]:
                                out.write("\t"+loc[:(len(loc)/2)])
                            else:
                                out.write("\t-9")
                            if loc[(len(loc)/2):] not in ["0","00","000"]:
                                out.write("\t"+loc[(len(loc)/2):])
                            else:
                                out.write("\t-9")
                    out.write("\n")
        c.close()
        out.close()
        
    
    
    

    
