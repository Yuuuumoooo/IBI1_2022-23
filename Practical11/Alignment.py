#import nessary packages
import re
import pandas as pd

#import three protein sequences
seq=open("ACE2_human.fa","r").read()
human=re.sub(r".+\n(.+)\n",r"\1",seq)

seq=open("ACE2_mouse.fa","r").read()
mouse=re.sub(r".+\n(.+)\n",r"\1",seq)

seq=open("ACE2_cat.fa","r").read()
cat=re.sub(r".+\n(.+)\n",r"\1",seq)

#import BLOSUM62
matrix=pd.read_excel(r"BLOSUM62.xlsx",index_col=0)

#compare human and mouse
score=0
for i in range(len(human)):
  col=human[i]
  raw=mouse[i]
  score+=matrix.loc[col,raw]
print("seq1=human\nseq2=mouse\nBLOSUM62 score=",score)

same=0
for i in range(len(human)):
  if human[i]==mouse[i]:
    same+=1
per=same/len(human)*100
print("the identical aa percentage is",per,"%\n")
  
#compare human and cat
score=0
for i in range(len(human)):
  col=human[i]
  raw=cat[i]
  score+=matrix.loc[col,raw]
print("seq1=human\nseq2=cat\nBLOSUM62 score=",score)
    
same=0
for i in range(len(human)):
  if human[i]==cat[i]:
    same+=1
per=same/len(human)*100
print("the identical aa percentage is",per,"%\n")

#compare mouse and cat
score=0
for i in range(len(mouse)):
  col=mouse[i]
  raw=cat[i]
  score+=matrix.loc[col,raw]
print("seq1=mouse\nseq2=cat\nBLOSUM62 score=",score)

same=0
for i in range(len(mouse)):
  if mouse[i]==cat[i]:
    same+=1
per=same/len(mouse)*100
print("the identical aa percentage is",per,"%\n")

#my interpretation
#Because human-cat has the largest score, the sequences of human and cat are most closely related.
#Human, mouse and cat are all closely related (>80%), probably because they share a common ancestor and they all evolved into mammals.
