class Parent_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name)
        print("age:",self.age)
class Child_class(Parent_class):
    def __init__(self,name,age,city):
        super().__init__(name,age)
        self.city=city
    def show(self):
       super().show()
       print("city:",self.city)

p=Parent_class("John",30)
p.show()
c=Child_class("John",30,"New York")
c.show()