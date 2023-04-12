import re

#ask for an input and create a file
stop=input("TAA/TAG/TGA:")
new_file=open(stop+"_stop_genes.fa","w")
file=open("xid-1055764_1")

sequence=""
for line in file:
  if not re.search(">",line):
    new_line=re.sub(r"(.+)$\n",r"\1",line)
    sequence+=new_line
  else:
    if re.findall(r"ATG.+"+stop,sequence):
      number=str(sequence.count(stop))
      new_name =" ".join(map(str,new_name))+" total number "+number+"\n"
                        #change to str type
      sequence+="\n\n"
      new_file.write(new_name)
      new_file.write(sequence)
    sequence=""
    new_name = re.findall(r"^>\S+",line)
new_file.close()
