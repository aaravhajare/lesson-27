class person () :

    def __init__(self,name,idnumber):

        self.name = name
        self.idnumber = idnumber

    def display(self) :

        print(self.name)
        print(self.idnumber)

class employee(person):

    def __init__(self, name, idnumber , post , salary):
        self.salary = salary
        self.post = post

        person.__init__(self , name , idnumber)

a = employee("Aahan" , 9999999999 , "fresher" , 0.9)

a.display()