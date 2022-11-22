class Person:
    def __init__(self,id): self.id = id


mary = Person(123)
mary.__dict__['age'] = 18
mary.__dict__['gender'] = 'female'
print(mary.age + len(mary.__dict__))