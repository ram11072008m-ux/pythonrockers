class employee:
    def __init__(self,name,eid,salary,experience,role):
        self.name = name
        self.eid = eid
        self.salary = salary
        self.experience = experience
        self.role = role

    def display(self):
        print("Name: ",self.name)
        print("Employee ID: ",self.eid)
        print("Salary: ",self.salary)
        print("Experience: ",self.experience)
        print("Role: ",self.role)
        print("\t-------------------------\t")
        
e1 = employee("Hari","emp22",75000,"3 years" ,"Software Developer")
e2 = employee("Anas","emp33",65000,"2 years" ,"database administrator")

e1.display()
e2.display()
