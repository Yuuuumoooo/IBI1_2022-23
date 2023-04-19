#create a function to calculate whether a DNA is likely to be protein coding
import re
def protein(DNA):
  """
  input: DNA sequence, a string, only one ATG start and one TGA stop codon
  if more than 50% of DNA is within these codons, return "protein-coding"
  if less than 10% of DNA is within these codons, return "non-coding"
  everything else return "unclear"
  """
  for i in re.finditer(r"ATG.+TGA",DNA,re.IGNORECASE):
    start=i.start()
    end=i.end()
  length=int(end)-int(start)
  ratio=length/len(DNA)
  if ratio > 0.5:
    print("this DNA is protein-coding")
  elif ratio < 0.1:
    print("this DNA is non-coding")
  else: 
    print("this DNA is unclear")

#an example
print("#this is an example with DNA sequence is AAAATGGGCCCAATGATTGGCA")
DNA_example="AAAATGGGCCCAATGATTGGCA"
protein(DNA_example)

DNA=input("input DNA sequence:")
protein(DNA)


