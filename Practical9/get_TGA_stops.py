import re
import os

#extract all genes with TGA stop codon
os.chdir("/Users/qiuliyan/Desktop/IBI/IBI1_2022-23/Practical9")  #change directory
file=open("xid-1055764_1")  #open file
new_file=open("TGA_genes.fa","w")  #create new file

sequence="" 
for line in file:
  if not re.search(">",line):  #sequence
    new_line=re.sub(r"(.+)$\n",r"\1",line)  #put the sequence into one variable without \n
    sequence+=new_line
  else:  #gene name
    if re.findall(r"ATG.+TGA$",sequence):
      new_name =" ".join(map(str,new_name))+"\n"  #change to str type
      sequence+="\n"
      new_file.write(new_name)
      new_file.write(sequence)
    sequence=""
    new_name = re.findall(r"^>\S+",line)
file.close()
new_file.close()
