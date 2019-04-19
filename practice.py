class Person(object):
    def __init__(self, name=None, job=None, quote=None):
        self.name = name
        self.job = job
        self.quote = quote


personList = list()
personDict = dict()

personList.append(Person("Payne N. Diaz", "coach", "Without exception, there is no rule!"))
personList.append(Person("Mia Serts", "bicyclist", "If the world didn't suck, we'd all fall off!"))
personList.append(Person("Don B. Sanosi", "teacher", "Work real hard while you wait and good things will come to you!"))
personList.append(Person("Hugh Jorgan", "organist", "Age is a very high price to pay for maturity."))

print(personList[0])

person1 = Person("Payne N. Diaz", "coach", "Without exception, there is no rule!")
person2 = Person("Mia Serts", "bicyclist", "If the world didn't suck, we'd all fall off!")
personDict[person1] = 1
personDict[person2] = 2

print(personDict)

for k in personDict:
    print(k)


