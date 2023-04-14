import re

#ask for an input and create a file
stop=input("TAA/TAG/TGA:")  #ask for a stop input
stop_codon=["TAA","TAG","TGA"]
file=open("xid-1055764_1") #open sequence file

if stop in stop_codon:
  new_file=open(stop+"_stop_genes.fa","w") #create a new file
  sequence=""
  for line in file:
    if not re.search(">",line):  #sequence
      new_line=re.sub(r"(.+)$\n",r"\1",line)
      sequence+=new_line
    else:  #gene name
      if re.findall(r"ATG.+"+stop+"$",sequence):
        number=str(sequence.count(stop))
        new_name =" ".join(map(str,new_name))+" total number "+number+"\n"
                         #change to str type
        sequence+="\n\n"
        new_file.write(new_name)
        new_file.write(sequence)
      sequence=""
      new_name = re.findall(r"^>\S+",line)
  new_file.close()
  file.close()
else: 
  print("input a wrong stop condon")
