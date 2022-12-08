"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

    def contract(self, type, salary, workingHours):
        self.contract =type
        self.salary = salary
        self.workingHours = workingHours

    def commission(self, type, bonus, contractNum):
        self.commission=type
        self.bonus=bonus
        self.contractNum=contractNum
    

    def get_pay(self):
        if self.contract == 'monthly':
            pay=self.salary
        else:
            pay=self.salary*self.workingHours
        if self.commission == 'contract':
            pay = pay+ self.bonus * self.contractNum
        elif self.commission =='fix':
            pay = pay+self.bonus
        return pay


    def __str__(self):
        text = self.name + ' works on a '
        if self.contract == 'monthly':
            text += 'monthly salary of '+str(self.salary)
        else:
            text += 'contract of '+str(self.workingHours)+ ' hours at '+str(self.salary)+'/hour'
        
        if self.commission == 'contract':
                text += ' and receives a commission for ' + str(self.contractNum) + ' contract(s) at ' + str(self.bonus) + '/contract.'
        elif self.commission == 'fix':
            text += ' and receives a bonus commission of ' + str(self.bonus) + '.'
        else:
            text += '.'
        text += '  Their total pay is ' + str(self.get_pay()) + '.'
        return text


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.contract('monthly', 4000, 0)
billie.commission('', 0, 0)
print (str(billie))
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.contract('hourly', 25, 100)
charlie.commission('', 0, 0)
print (str(charlie))


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.contract('monthly', 3000, 0)
renee.commission('contract', 200, 4)
print (str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.contract('hourly', 25, 150)
jan.commission('contract', 220, 3)
print (str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.contract('monthly', 2000, 0)
robbie.commission('fix', 1500, 0)
print (str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.contract('hourly', 30, 120)
ariel.commission('fix', 600, 0)
print (str (ariel))
