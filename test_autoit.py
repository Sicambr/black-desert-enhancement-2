
class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


x = FirstClass()
y = FirstClass()

x.setdata(45)
x.display()


z = SecondClass()
z.data = 999
z.display()

the_way = "https://www.youtube.com/watch?v=-_kFDmYlcs4&t=3s"
