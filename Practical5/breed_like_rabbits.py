#Two rabbits breed to produce two new rabbits
#so the number of the new born rabbits=total rabbits/2*2
#when finish one loop, that means finish one generation, so it should +1

total_number=2
generation=1
while total_number<100:
    newborn=total_number/2*2
    total_number+=newborn
    generation+=1
    print(newborn," rabbits are born in the generation ",generation)

print("At generation",generation," over 100 rabbits have been born.")
