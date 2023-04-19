#creat a new function to calculate whether a person can buy a house 
def affordability(house,salary):
  """
  Input: house, a positive int means the total value of the house
         salary, a positive int means the purchaser's annual salary
  Returns "Yes" if the house is no more than five times salary,
  else returns "NO"
  """
  house=int(house)   #change the type so that can ask for an input if needed
  salary=int(salary)  
  if house <= 5*salary:
    print("Yes, you can buy this house.")
  else:
    print("No, you cannot buy this house.")
  return house,salary

#an example
print("this is an example with house=180000 and salary=35000")
house=180000
salary=35000
affordability(house,salary)
##'No, you cannot buy this house.'

#ask for an input and calculate
house=input("What's the total value of the house? A:")
salary=input("What's your annual salary? A:")
affordability(house,salary)
