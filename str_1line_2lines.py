#README
#this script converts structure 1 line per individual format into 2 lines per individual format
#how many columns are there before the genotypes?
ncol=2
#write your file name
fich=open("str_30loc_ALL.str","r")
#write desired output name
out=open("str_30loc_2lines.str","w")
#does the file include the loci name header (1) or not (0):
genstart=1
linhas=fich.readlines()
if genstart==1:
    out.write(linhas[0])
for i in linhas[genstart:]:
    j=i.split("\t")
    for n in range(ncol):
        out.write(j[n]+"\t")
    out.write(j[ncol])
    for um in range(ncol+2,len(j),2):
        out.write(" "+j[um])
    out.write("\n")
    for n in range(ncol):
        out.write(j[n]+"\t")
    out.write(j[ncol+1])
    for dois in range(ncol+3,len(j)+1,2):
        out.write(" "+j[dois])
fich.close()
out.close()

    
    
