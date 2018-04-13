#This script takes a batch of structure files (format: 2 lines per individual, first two columns separated by tabs and genotype data separated by blank space) and converts the files to newhybrids format
#The outputs of the script will be a file in newhybrids format ("filename.nh") and a correspondence between individual names in the original and output files
#the default missing data format is "-9", change it below:
missing_data = "-9"
#does the structure file include the loci line (yes = 1 / no = 0)?
genstart=0
#b is the list of all files in the same folder where the script is:
import os
a=os.getcwd()
b=os.listdir(a)
b.remove("str-nh_2lines.py")
#or type the name of your files below and uncomment the line
#b=["yourfilename1.str","yourfilename2.str"]
for fich in b:
    
    f=file(fich,"r")
    out=file(fich+".nh","w")
    corr=file(fich+".corr","w")
    li=f.read()
    l=li.split("\n")[genstart:]
    numlines=0
    for line in l:
        if line != "":
            numlines+=1
    numindivs=numlines/2
    t=l[1].split("\t")[2].split(" ")
    numloc=len(t)
    ndig=len(t[0].replace(" ",""))
    out.write("NumIndivs "+str(numindivs)+"\nNumLoci "+str(numloc)+"\nDigits "+str(ndig)+"\nFormat NonLumped\n")
    corr.write("Structure\tNew hybrids\n")
    i=0
    for linha in range(numindivs):
        if l[2*linha] not in [""," ","\t","\n"]:
            if l[2*linha+1] not in [""," ","\t","\n"]:
                x=l[2*linha].split("\t")[2].split(" ")
                y=l[2*linha+1].split("\t")[2].split(" ")
                corr.write(l[2*linha].split("\t")[0]+"\t"+str(i)+"\n")
                out.write(str(i)+" ")
                for it in range(numloc):
                    if x[it] != missing_data:
                        out.write("  "+x[it])
                    else:
                        out.write("  -1")
                    if y[it] != missing_data:
                        out.write("  "+y[it])
                    else:
                        out.write("  -1")
            
            out.write("\n")
            i+=1
    out.close()

        
        
        
        
    
    
    
        
    
