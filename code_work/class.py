class Person:
    def greet(self):
        print("Hello ", self.name)
    def set_name(self, name):
        self.name=name
p1=Person()
p1.set_name("Ashish")
p1.greet()