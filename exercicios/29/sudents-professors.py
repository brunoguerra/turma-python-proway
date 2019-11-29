class Person:
    def __init__(self):
        print('More one person on this world', self)
        self.addresses = []
        self.__personAddress = None

    def set_lives_at(self, personAddress):
        self.__personAddress = personAddress
        self.addresses.append(personAddress)
    
    def get_lives_at(self):
        return self.__personAddress

    def add_address(self, address):
        self.addresses.append(address)

    def get_addresses(self):
        return self.addresses
    
    def getAddress(self):
        return self.personAddress    

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def getTelefone(self):
        return self.telefone
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def purchaseParkingPass(self):
        print(f'{self.nome} buyed a pass')

class Student(Person):
    def setStudentNumber(self, studentNumber):
        self.studentNumber = studentNumber
    
    def getStudentNumber(self):
        return self.studentNumber
    
    def setAverageMark(self, averageMark):
        self.averageMark = averageMark
    
    def getAverageMark(self):
        return self.averageMark
    
    def ValidateAverage(self):
        if self.getAverageMark() < 70:
            return 'REPROVADO'
        else:
            return 'APROVADO'
    
    def isEligible(self):
        print(f'{self.nome} é elegível')
    
    def getSeminarsTaken(self):
        print(['Python for Snakes', 'Java for Special kids', 'C++ for chips'])

class Professor(Person):
    def setSalary(self, salary):
        self.salary = salary
    
    def getSalary(self):
        return self.salary
    
class Address():
    def __init__(self, street='', city=''):
        self.setCity(city)
        self.setStreet(street)

    def setStreet(self, street):
        self.street = street
    
    def getStreet(self):
        return self.street
    
    def setCity(self, city):
        self.city = city
    
    def getCity(self):
        return self.city
    
    def setState(self, state):
        self.state = state
    
    def getState(self):
        return self.state
    
    def setPostalCode(self, postalCode):
        self.postalCode = postalCode
    
    def getPostalCode(self):
        return self.postalCode
    
    def __repr__(self):
        return self.street
    def x__repr__(self):
        return str(self.street) + "\n" + str(self.city) + "\n" + str(self.state) + "\n" + str(self.postalCode) + "\n" + str(self.country) + "\n"

    def setCountry(self, country):
        self.country = country
    
    def getCountry(self):
        return self.country
    
    def validate(self):
        pass

    def OutputAsLabel(self):
        pass

#Instanciando os objetos
student = Student()

student.setNome('Douglas')
student.setAverageMark(99)

student.purchaseParkingPass()

student.isEligible()

#Setando parametros ADDRESS
address = Address()
address.setStreet('Rua 7 de Setembro')
address.setCity('Blumenau')
address.setState('SC')
address.setPostalCode('89070-258')
address.setCountry('Brazil')

#Setando um ADDRESS para um STUDENT
# student.livesAt(address)
print(student.__personAddress)
print('-'*10)
print(student.get_lives_at())

student.set_lives_at(address)

for address in student.get_addresses():
    print('Address in student', address)












    # print('='*20)
    # print('='*20)

    # print(student.getAddresses())

    # print('='*20)
    # print('='*20)


    # address2 = Address()
    # address2.setStreet('Rua 8 de Setembro')
    # address2.setCity('Blumenau')
    # address2.setState('SC')
    # address2.setPostalCode('89080-258')
    # address2.setCountry('Brazil')

    # #Setando um ADDRESS para um STUDENT
    # student.addAddress(address2)

    # print('='*20)
    # print('='*20)

    # print(student.getAddresses())

    # print('='*20)
    # print('='*20)


    # address = Address()
    # address.setCity('Blumenau')
    # address.setStreet('Rua 9 de Setembro')

    # professor = Professor()
    # professor.setNome('Roberto')
    # professor.setTelefone('99999999')
    # professor.setEmail('roberto@')
    # professor.setSalary(25000.00)
    # professor.addAddress(address)

    # print(professor.getAddresses())
    #         # street='Rua b',

    # professor.addAddress(
    #     Address(
    #         city='Blumenau',
    #     )
    # )
    # print(professor.getAddresses())

    # print('Cidade é:')
    # print(professor.getAddresses()[-1].city)

# print(student.getAddress())

# print(type(student) is Student)
# print(type(professor) is Professor)
# print(type(student).__bases__)
# print(Person in type(student).__bases__)

# def print_name(person):
#     print(f'Name is: {person.nome}')

# print_name(student)
# print_name(professor)