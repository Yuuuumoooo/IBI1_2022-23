#creat a class
class triathlon(object):
  def __init__(self,first_name,last_name,location,swim,cycle,run,total):
    self.first_name=first_name
    self.last_name=last_name
    self.location=location
    self.swim=swim
    self.cycle=cycle
    self.run=run
    self.total=total
  def information(self):
    x="__dict__"
    value=self.__getattribute__(x)
    print(value)
    return self

#an example
person1=triathlon("Chen","Yumo","Haining","3'10''","5'20''","4'30''","13'00''")
print("the swim time of person1 is", person1.swim)
person1.information()
##the swim time of person1 is 3'10''
##{'first_name': 'Chen', 'last_name': 'Yumo', 'location': 'Haining', 'swim': "3'10''", 'cycle': "5'20''", 'run': "4'30''", 'total': "13'00''"}

