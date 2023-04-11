import re

#count total number
seq="ATGCAATCGACTACGATCTGAGAGGGCCTAA"
count=0
if re.findall(r"^ATG.+TAA",seq):
  count+=1
if re.findall(r"^ATG.+TAG",seq):
  count+=1
if re.findall(r"^ATG.+TGA",seq):
  count+=1
print(count)
