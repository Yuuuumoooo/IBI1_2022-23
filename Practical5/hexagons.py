#I have known the nth hexagonal number(overall number)
#I want to calculate the nth number (outmost number) in the hexagon sequence.
#the increased dots = nth hexagonal number - (n-1)th hexagonal number
#the dots shared by nth and (n-1)th increase 2 when n increase 1 (n>=3)

#for the 1st layer, the hexagon number equals its sequence number
a=2*1*(2*1-1)/2
print(a)
#for the 2nd layer, the number of shared dots is 1
shared=1
for n in range (2,6):
    increased=2*n*(2*n-1)/2-2*(n-1)*(2*(n-1)-1)/2
    overall=increased + shared
    print(overall)
    shared=shared+2
