class student(object):

    nstudents = 0
    schoolname = ''

    # Data/attributes
    def __init__(self, name, cls, rid):
        print('Initializing values.....')
        # [TASK 1]Identify and write all the variables needed here
        student.nstudents += 1

    # [TASK 2]Complete the functions/methods

    def setschoolname(self, schoolname):
        pass

    def printinfo(self):
        self.state = 'Karnataka'
        print('STATE : ', self.state)
        print('SCHOOL: ', student.schoolname)
        print('-----------------------------------')
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.maths)
        print('PHYSICS  : ', self.physics)
        print('CHEMISTRY: ', self.chemistry)
        print('BIOLOGY  : ', self.biology)
        print('-----------------------------------')
        print('AVERAGE  : ', self.average)
        print('NSTUDENTS  ------> ', student.nstudents)
        print('\n')

    def setMaths(self, marks):
        pass

    def setPhysics(self, marks):
        pass

    def setChemistry(self, marks):
        pass

    def setBiology(self, marks):
        pass

    def calcAverage(self):
        pass

#######################################################################################

if __name__ == '__main__':

    s1 = student('Rohit', 12, 'A001')
    #s1.printinfo()

    s2 = student('Sunil', 12, 'A002')
    #s2.printinfo()

    s3 = student('Anil', 12, 'A003')
    #s3.printinfo()



    
    s1.setschoolname('St. Josephs\'s School')

     

    s1.printinfo()
    s2.printinfo()
    s3.printinfo()


    print("-"*100)

    s1.setPhysics(78)
    s1.setMaths(99)
    s1.setChemistry(98)
    s1.setBiology(97)

    s1.printinfo()
    s2.printinfo()
    s3.printinfo()

    print("-"*100)

    s1.setschoolname('Kendriya Vidyalaya')

    s1.calcAverage()
    s1.printinfo()
    s2.printinfo()
    s3.printinfo()

    
    # ----------------------------------------
    s4 = student('Aproop', 12, 'A002')
 

    s4.setPhysics(90)
    s4.setMaths(95)
    s4.setChemistry(98)
    s4.setBiology(99)
   

    s4.calcAverage()
    s4.printinfo()

    print("-"*100)

    
    # ----------------------------------------
    s5 = student('Rajesh', 12, 'A008')

    s5.setPhysics(100)
    s5.setMaths(96)
    s5.setChemistry(98)
    s5.setBiology(97)
    

    s5.calcAverage()
    s5.printinfo()




    

    print(s1.nstudents, s2.nstudents, student.nstudents)


   