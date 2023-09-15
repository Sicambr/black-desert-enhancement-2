class Firstclass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class Secondclass(Firstclass):
    def display(self):
        print('Current value = "%s"' % self.data)


class rec:
    pass


x = Firstclass()
y = Firstclass()

x.setdata('King Artur')
y.setdata(34)

x.display()
y.display()

x.data = ('nemo')
x.display()

x.anonthername = 'lel'
print(x.anonthername)

z = Secondclass()
z.setdata(42)
z.display()

x = rec()
rec.name = 'Bob'
y = rec()
print(x.name)
print(y.name)
print(rec.__dict__)
