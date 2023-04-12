import re

#count total number
seq="ATGCAATCGACTACGATCTGAGAGGGCCTAA"
stop=["TAA","TAG","TGA"]
total=0

for i in stop: 
  count=seq.count(i)
  total+=count
print(total)
