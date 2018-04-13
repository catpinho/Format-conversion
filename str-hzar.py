#this script converts from structure format into hzar format
#the acceptable structure format is 2 lines per individual, first individual names, populations and 1st genotype columns separated by tabs, genotypes separated by whitespace 
#########################################################################
######## FILL INFO IN THIS HEADER  ######################################
#########################################################################
#input
fich=file("yourfilename.str","r").read().split("\n")
#missing data
missing_data="-9"
#is the locus line included?
genstart = 1
#populations to include as in the structure file
pops_to_include=["1","2","3","4","5","6","7","8"]
#distances (number of items needs to match the number of populations
distances=[0,6590,7770,10760,14100,18520,21700,44510]
#output
out=file("youroutfilename.hzar","w")
#########################################################################

def calcula_freqs(pops,loc):
    #loc é uma lista de pops a contar
    #o loc é o valor absoluto (conta com todos os outros loci também)
    altypes=[]

    freqs=[]

    counts=[]
    for pop in pops:

        alls=[]
        
        m=pop.split("+")
        for line in fich[genstart:]:
            if line != "":
                if line.split("\t")[1] in m:
                    x=line.split("\t")[2].split(" ")[loc]
                    if x!=missing_data:
                        alls.append(x)
                        if x not in altypes:
                            altypes.append(x)

        counts.append(alls)


    if len(altypes)>2:
        print altypes
        print str(loc)+" NOT DIALLELIC"
    for pop in range(len(pops)):
        if len(counts[pop])!=0:
            freqs.append([counts[pop].count(altypes[0])*1.0/len(counts[pop]),len(counts[pop])])
        else:
            freqs.append(["NA","NA"])
    return freqs
if genstart == 1:
    loc=fich[0].split("\t")[2].split("  ")
else:
    loc=[]
    x=1
    for u in fich[0].split("\t")[2].split(" "):
        loc.append("loc"+str(x))
        x+=1
        

out.write("Population\tDistance")
for l in loc:
    out.write("\t"+l+".A\t"+l+".B\t"+l+".N")
out.write("\n")

freqstotais=[]
for l in range(len(loc)):

    freqstotais.append(calcula_freqs(pops_to_include,l))
for pop in pops_to_include:
    out.write(str(pop)+"\t"+str(distances[pops_to_include.index(pop)]))

    for l in range(len(loc)):
        if freqstotais[l][pops_to_include.index(pop)][0]!="NA":
            out.write("\t"+str(round(freqstotais[l][pops_to_include.index(pop)][0],3))+"\t"+str(round(1-freqstotais[l][pops_to_include.index(pop)][0],3))+"\t"+str(freqstotais[l][pops_to_include.index(pop)][1]))
        else:
            print loc[l]
 	    out.write("\tNA\tNA\t0")
    out.write("\n")
out.close()
              
        
    


    
