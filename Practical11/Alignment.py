#import nessary packages
from Bio import pairwise2
from Bio.Align import substitution_matrices
import re

#import three protein sequences
species=["human","mouse","cat"]
pro={}
for i in species:
  file=open("ACE2_"+i+".fa","r")
  seq=file.read()
  pro[i]=re.sub(r".+\n(.+)\n",r"\1",seq)
  file.close()

#reference:https://biopython.org/docs/1.75/api/Bio.pairwise2.html
#import BLOSUM62 matrix
matrix=substitution_matrices.load("BLOSUM62")

#alignment
human_mouse=pairwise2.align.globaldx(pro["human"],pro["mouse"],matrix)
score1=human_mouse[0][2]
hm=pairwise2.align.globalxx(pro["human"],pro["mouse"])
perc1=hm[0][2]/len(pro["human"])

human_cat=pairwise2.align.globaldx(pro["human"],pro["cat"],matrix)
score2=human_cat[0][2]
hc=pairwise2.align.globalxx(pro["human"],pro["cat"])
perc2=hc[0][2]/len(pro["human"])

mouse_cat=pairwise2.align.globaldx(pro["mouse"],pro["cat"],matrix)
score3=mouse_cat[0][2]
mc=pairwise2.align.globalxx(pro["mouse"],pro["cat"])
perc3=mc[0][2]/len(pro["mouse"])

#print the findings
print("human and mouse have score",score1,"in protein sequence length of",len(pro["human"]),"with overlap percentage of",perc1,"\n",human_mouse[0][1])
print("human and cat have score",score2,"in protein sequence length of",len(pro["human"]),"with overlap percentage of",perc2,"\n",human_cat[0][1])
print("mouse and cat have score",score3,"in protein sequence length of",len(pro["mouse"]),"with overlap percentage of",perc3,"\n",mouse_cat[0][1])

#my interpretation
#Because human_mouse has the largest score, the sequences of human and mouse are most closely related.
#Human, mouse and cat are all closely related, probably because they share a common ancestor and they all evolved into mammals.
